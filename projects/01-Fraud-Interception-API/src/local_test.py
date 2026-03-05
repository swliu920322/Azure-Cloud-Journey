import json
import xgboost as xgb
import numpy as np
import yaml
import time

# 1. 读取架构约束
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

print("[SYSTEM] Loading XGBoost Engine from local storage...")
model = xgb.XGBClassifier()
model.load_model(config['paths']['xgb_model'])

CRITICAL_THRESHOLD = config['thresholds']['critical_api_lock']
VERIFICATION_THRESHOLD = config['thresholds']['mfa_verification']


def simulate_api_request(mock_features):
    print("\n[NETWORK] Receiving synthetic transaction payload...")
    start_time = time.perf_counter()

    # 核心推理动作
    risk_score = float(model.predict_proba(mock_features)[:, 1][0])

    # 路由矩阵判断
    if risk_score >= CRITICAL_THRESHOLD:
        action = "API_LOCK_EXECUTED (Critical Threat)"
    elif risk_score >= VERIFICATION_THRESHOLD:
        action = "MFA_SMS_TRIGGERED (Verification Zone)"
    else:
        action = "PASSIVE_LOGGING_CLEARED (Safe)"

    end_time = time.perf_counter()
    latency_ms = (end_time - start_time) * 1000

    print(f"--> Calculated Risk Score : {risk_score:.4f}")
    print(f"--> Action Triggered      : {action}")
    print(f"--> Local Compute Latency : {latency_ms:.2f} ms")


if __name__ == "__main__":
    # 构造一个 30 维的假数据向量 (模拟清洗后的 V1-V28, scaled_amount, scaled_time)
    # 模拟一笔安全交易
    print("\n--- TEST CASE 1: Normal Transaction ---")
    safe_payload = np.zeros((1, 30))
    simulate_api_request(safe_payload)

    # 模拟一笔极端异常的欺诈交易 (强行拉高特征值)
    print("\n--- TEST CASE 2: High-Risk Fraud Transaction ---")
    fraud_payload = np.random.uniform(5.0, 15.0, size=(1, 30))
    simulate_api_request(fraud_payload)