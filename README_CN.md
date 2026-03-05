# Azure Cloud Journey: Engineering the AI-Native Future

这是我从 **10年前端老兵** 向 **企业级 AI 云架构师** 进化的物理记录。这里不存储零散的代码片段，只存放经过压测验证的、可落地的云原生架构方案（PoC）。

## 🎯 核心目标 (Roadmap)
* **阶段 1 (2025-2026):** 攻克 Azure AI 与数据工程闭环。目标证书：`AI-102`, `AZ-305`。
* **阶段 2 (2026):** 落地新加坡。专注于高并发金融风控与企业级 RAG 架构。

## 🏗 已落地项目 (Portfolio)
### 01. Low-Latency Fraud Interception API
* **核心突破:** 解决了银行网关 50ms 超时限制下的实时风险拦截。
* **物理指标:** 22ms 响应延迟 / 92.86% 拦截召回率。
* **技术栈:** Azure Functions, APIM, XGBoost.
* **[查看项目详情](./projects/01-Fraud-Interception-API/)**

## 🧠 架构决策记录 (Architecture Decision Records)
我坚持记录每一次重大技术选择背后的逻辑，拒绝盲目调包。
* [ADR-001: 放弃 RPA GUI 路径，执行 API-First 实时拦截](./ADRs/ADR-001-Fraud-API-API-First.md)

---
"In Cloud Architecture, we don't guess. We measure."