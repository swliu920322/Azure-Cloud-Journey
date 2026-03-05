import pandas as pd
import yaml
import joblib
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split
import os

# 1. 加载物理约束
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)


def execute_pipeline():
    print("[SYSTEM] Initiating training pipeline...")

    # 2. 数据摄取与特征缩放 (RobustScaler 保护极值)
    df = pd.read_csv(config['paths']['data_source'])
    scaler = RobustScaler()
    df['scaled_amount'] = scaler.fit_transform(df['Amount'].values.reshape(-1, 1))
    df['scaled_time'] = scaler.fit_transform(df['Time'].values.reshape(-1, 1))
    df.drop(['Time', 'Amount'], axis=1, inplace=True)

    X = df.drop('Class', axis=1)
    y = df['Class']

    # 3. 隔离测试集，对训练集执行 SMOTE
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
    print("[SYSTEM] Executing SMOTE topology rewrite...")
    sm = SMOTE(sampling_strategy='minority', random_state=42)
    X_train_sm, y_train_sm = sm.fit_resample(X_train, y_train)

    # 4. 强制约束 XGBoost 深度，避免网关超时
    print("[SYSTEM] Compiling XGBoost engine...")
    model = XGBClassifier(
        max_depth=config['model_params']['max_depth'],
        learning_rate=config['model_params']['learning_rate'],
        n_estimators=config['model_params']['n_estimators'],
        n_jobs=-1,
        random_state=42
    )
    model.fit(X_train_sm, y_train_sm)

    # 5. 固化模型资产
    os.makedirs('model', exist_ok=True)
    model.save_model(config['paths']['xgb_model'])
    joblib.dump(scaler, config['paths']['scaler'])
    print(f"[SUCCESS] Model hardcoded to {config['paths']['xgb_model']}")


if __name__ == "__main__":
    execute_pipeline()