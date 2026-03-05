# ADR-001: Bypassing RPA GUI for API-First Real-Time Interception

* **Status:** Accepted
* **Date:** 2026-03-05
* **Decider:** Liu Shengwei (戊土)

---

## Part I: English Architecture Documentation

### 1. Context & Problem Statement
Financial institutions operate under a critical **50ms latency gateway**. Existing solutions often rely on RPA tools (e.g., UiPath) to simulate human GUI interactions for account freezing. However, GUI rendering and element location incur multi-second delays, leading to "Semantic Blindness"—where fraud is predicted, but funds are cleared before the action is executed.

### 2. Decision Drivers
* **Latency First:** The end-to-end execution must be sub-30ms to ensure the gateway is intercepted.
* **Data Imbalance:** Handling 0.173% fraud minority class without losing topological features.
* **Zero Manual Intervention:** Eliminating human cognitive fatigue in high-velocity streams.

### 3. Considered Options

#### Option 1: Legacy RPA GUI Execution
* **Cons:** Latency > 2000ms. High failure rate due to UI volatility.
* **Result:** **REJECTED** due to physical latency constraints.

#### Option 2: Deep Learning (MLP/GNN)
* **Pros:** Slightly higher accuracy in static testing.
* **Cons:** Matrix multiplication on CPU creates 20ms+ inference overhead.
* **Result:** **REJECTED** to reserve latency budget for network handshake.



#### Option 3: XGBoost + API-First Serverless
* **Pros:** Sub-2ms local inference; Direct REST API calls to banking backends.
* **Result:** **ACCEPTED** as the primary architectural path.

### 4. Proposed Solution
We implement an **API-First Routing Matrix** deployed on **Azure Functions**:
1. **Feature Engineering:** Use `RobustScaler` to preserve financial outliers and `SMOTE` for minority oversampling in training.
2. **Inference:** Deploy a constrained `XGBoost` model (`max_depth=6`) to minimize compute cycles.
3. **Execution:** If `Risk_Score >= 0.90`, the system bypasses all GUI layers and directly triggers the `/api/v1/account/lock` endpoint via a secure REST call.

### 5. Consequences & Metrics
* **Execution Speed:** Latency dropped to **22ms** (P95), clearing the 50ms gateway deathline.
* **Precision/Recall:** Achieved **92.86% Recall** for critical fraud.
* **User Friction:** Verification friction limited to **2.89%** of legitimate traffic.

<p>
  <img src="../projects/01-Fraud-Interception-API/assets/delay.png" alt="22ms Latency Proof" width="500">
  <br>
  <i>Figure 1: Postman latency verification (Clocked at 22ms)</i>
</p>
---

## 第二部分：中文架构决策复盘

### 1. 背景与问题陈述
金融机构面临极其苛刻的 **50ms 结算网关死线**。 现有方案多依赖 RPA 工具（如 UiPath）模拟人工 GUI 操作来执行账户冻结。 然而，GUI 渲染和元素定位会产生秒级延迟，导致“语义失明”：即预测到了欺诈，但在执行拦截前资金已完成清算。

### 2. 决策驱动因素
* **延迟优先：** 端到端执行必须在 30ms 内，以确保网关拦截成功。
* **数据失衡：** 处理 0.173% 的极少数欺诈类数据，且不丢失拓扑特征。
* **零人工干预：** 消除高频交易流中的人工认知疲劳。

### 3. 候选方案对比
* **方案 1：传统 RPA GUI 执行。** 延迟 > 2000ms，因物理延迟限制被**否决**。
* **方案 2：深度学习 (MLP/GNN)。** CPU 矩阵运算产生超过 20ms 的推理开销，为保留网络握手带宽而被**否决**。
* **方案 3：XGBoost + API-First 无服务器架构。** 具备亚毫秒级本地推理能力，通过 REST API 直连银行后端，被**采纳**为核心路径。

### 4. 最终决策方案
我们执行部署在 **Azure Functions** 上的 **API-First 路由矩阵**：
1. **特征工程：** 使用 `RobustScaler` 保护金融异常值拓扑，并在训练环节使用 `SMOTE` 进行过采样。
2. **推理：** 部署受限 `XGBoost` 模型（`max_depth=6`）以最小化计算周期。
3. **执行：** 若风险评分 $\ge 0.90$，系统绕过所有 GUI 层，直接触发底层账户锁定接口。

### 5. 结果与物理指标
* **执行速度：** 延迟降至 **22ms**，成功切入 50ms 网关死线。
* **拦截召回率：** 核心欺诈拦截率达到 **92.86%**。
* **用户摩擦：** 合法流量的验证摩擦率严格控制在 **2.89%**。

---
"In Cloud Architecture, the only truth is the latency log."

