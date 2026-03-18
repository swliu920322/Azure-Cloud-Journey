## **[ADR-002: Implementation of Asymmetric ML Funnel & RAG Latency Trade-offs]**

**Status:** Accepted
**Date:** 2026-03-17
**Context:** `projects/02-Agentic-RPA-Compliance`

**1. Context & Decision Drivers**
Traditional rule-based RPA suffers from semantic blindness, generating massive false positives against structured "smurfing" tactics. Manual compliance review of 10,000 transactions requires ~22.2 hours. We require an architecture that automates decisions while maintaining ultra-low latency and strict legal explainability.

- **Throughput:** Must process high-frequency API streams without compute bottlenecks.
- **Explainability:** Black-box AI is legally void. Actions must map to statutory AML texts.
- **Execution Resilience:** Reject fragile UI-automation. Force industrial-grade API integration.

**2. Proposed Solution: The Adapter Theory in Action**
We deployed a four-tier architecture acting as an "Adapter" to convert AI probability into physical execution:

- **Stage 1 (Data Minimization):** Ingress tokenization strips PII via MD5 hashing before ML ingestion.
- **Stage 2 (Asymmetric ML Funnel):** Isolation Forest (iForest) clears 95% of routine traffic in memory (~5s). Support Vector Machine (SVM) executes heavy hard-margin cuts strictly on the remaining 5% outliers (~10s).
- **Stage 3 (Cognitive RAG):** Cross-references SVM outliers against an AML vector database to generate human-readable legal evidence.
- **Stage 4 (API-First RPA):** Bypasses UI entirely. Triggers `HTTP POST /api/lockBusiness` to freeze assets directly.

**3. Physical Trade-offs & Consequences**

- **Throughput Impact:** Pipeline latency dropped from 22.2 hours to 8.5 minutes (155x improvement).
- **RAG Latency Compromise:** *Crucial Trade-off*. Initial tests showed massive vector retrieval spikes gateway latency. We enforced strict data minimization: the RAG module operates as an asynchronous 'cold-path', triggered ONLY when SVM confidence > 0.8. We trade absolute, comprehensive legal context for required sub-second physical execution.
- **Azure Mapping Readiness:** Architecture explicitly mirrors AZ-305 targets (Azure APIM, Azure Machine Learning, Azure AI Search, Logic Apps), securing cross-cloud scalability.
---

## **[ADR-002: 基于非对称 ML 漏斗与 RAG 延迟妥协的实时拦截架构]**

**状态：** 已接受
**日期：** 2026-03-17
**上下文：** `projects/02-Agentic-RPA-Compliance`

**1. 背景与决策驱动力**
传统规则型 RPA 存在严重的语义盲区。在应对“蓝精灵”结构化洗钱时，会产生毁灭性的误报率。压测显示，人工审查 10,000 条交易需耗时约 22.2 小时。我们需要一套能在毫秒级延迟下实现自动化决策，并保持绝对法律可解释性的系统。

- **吞吐量：** 必须在无算力瓶颈的情况下处理高频 API 数据流。
- **可解释性：** 黑盒 AI 在金融界不具备法律效力。拦截动作必须有法定反洗钱文本支撑。
- **执行韧性：** 彻底抛弃脆弱的 UI 自动化。强制执行工业级 API 对接。

**2. 架构决策：适配器理论的物理落地**
我们部署了四层架构，作为将 AI 概率转换为物理动作的“适配器 (Adapter)”：

- **阶段 1 (数据极小化)：** 入口层强制执行 MD5 散列，在进入 ML 引擎前剥离所有 PII 敏感数据。
- **阶段 2 (非对称 ML 漏斗)：** 隔离森林 (iForest) 在内存中瞬间清空 95% 常规流量 (约 5 秒)。支持向量机 (SVM) 将高维硬边缘切割严格限制在剩余 5% 的异常点上 (约 10 秒)。
- **阶段 3 (认知 RAG)：** 将 SVM 圈定的异常特征与 AML 向量数据库交叉比对，生成人类可读的法定证据。
- **阶段 4 (API 优先执行)：** RPA 机器人彻底绕过 UI。异步触发 `HTTP POST /api/lockBusiness`，在网关层执行物理级资产冻结。

**3. 物理妥协与后果**

- **吞吐量收益：** 压测耗时从 22.2 小时断崖式暴跌至 8.5 分钟 (吞吐量飙升 155 倍)。
- **RAG 延迟妥协 (核心决策)：** 压测表明，无限制的 RAG 向量检索会产生极高 IOPS，直接拖垮网关响应。我们强制执行降级策略：RAG 降维为异步“冷路径”，仅在 SVM 置信度 > 0.8 时触发。用牺牲绝对全局上下文的代价，换取网关必须的亚秒级执行速度。
- **Azure 云原生对齐：** 架构全量映射 AZ-305 组件库 (Azure APIM, Azure ML Workspace, Azure AI Search, Logic Apps)，为后续跨云架构打通物理底层。