# Enterprise Fraud Interception API (Azure-Native Architecture)
# (企业级金融反欺诈拦截 API - 云原生架构)

## ⚡ Performance Benchmark (性能实证)

**English:** To validate the sub-30ms architectural requirement, we executed a full-stack pressure test on the Azure Function (Consumption Plan). The end-to-end latency, including network handshake and XGBoost inference, is stabilized at **22ms**.

**中文：** 为验证 30ms 以内的架构需求，我们在 Azure Function（消耗计划）上执行了全栈压力测试。包含网络握手与 XGBoost 推理在内的端到端延迟稳定在 **22ms**。

<p align="left">
  <img src="assets/delay.png" alt="22ms Latency Proof" width="500">
  <br>
  <i>Figure 1: Postman latency verification (Clocked at 22ms)</i>
</p>

---

## 🏗 System Architecture (系统架构)



### Key Modules (核心模块):
1. **Inference Engine (`src/inference_api.py`):** Stateless Python handler optimized for cold-start mitigation.
2. **Training Pipeline (`src/train_pipeline.py`):** Implements SMOTE and RobustScaler for topological integrity.
3. **Control Plane (`config.yaml`):** Centralized threshold management for risk-routing.

---

## 🚀 Deployment (部署)

1. **Local Sandbox (本地沙盒):**
   ```bash
   pip install -r requirements.txt
   python src/train_pipeline.py
   python local_test.py