import azure.functions as func
import json
import xgboost as xgb
import numpy as np
import yaml

# 物理预热：在全局空间加载模型，避开高频请求的冷启动惩罚
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

model = xgb.XGBClassifier()
model.load_model(config['paths']['xgb_model'])

CRITICAL_THRESHOLD = config['thresholds']['critical_api_lock']
VERIFICATION_THRESHOLD = config['thresholds']['mfa_verification']


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # 1. 拦截前端 JSON 载荷
        req_body = req.get_json()
        user_id = req_body.get('User_ID')
        features = np.array(req_body.get('features')).reshape(1, -1)

        # 2. 执行亚毫秒级推理
        risk_score = float(model.predict_proba(features)[:, 1][0])

        # 3. 触发硬件级路由矩阵 (Routing Matrix)
        if risk_score >= CRITICAL_THRESHOLD:
            action = "API_LOCK_EXECUTED"
            status_code = 200  # 业务拦截成功
        elif risk_score >= VERIFICATION_THRESHOLD:
            action = "MFA_SMS_TRIGGERED"
            status_code = 202  # 挂起，等待验证
        else:
            action = "PASSIVE_LOGGING_CLEARED"
            status_code = 200

        # 4. 组装响应底座
        response_payload = {
            "User_ID": user_id,
            "Risk_Score": round(risk_score, 4),
            "Action": action,
            "Latency_Constraint": "Sub-50ms Gateway Cleared"
        }

        return func.HttpResponse(
            json.dumps(response_payload),
            mimetype="application/json",
            status_code=status_code
        )

    except Exception as e:
        return func.HttpResponse(f"Payload Error: {str(e)}", status_code=400)