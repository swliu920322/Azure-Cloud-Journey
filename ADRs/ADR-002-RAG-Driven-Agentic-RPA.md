# ADR-002: Implementation of Asymmetric ML Funnel (iForest + SVM) for Real-time Interception

**Status:** Accepted
**Date:** 2026-03-05
**Context:** `projects/02-Agentic-RPA-Compliance`

## 1. Context
Traditional rule-based RPA systems are too rigid to handle sophisticated fraud like "smurfing." They generate excessive false positives and cause cognitive fatigue for human reviewers. In our simulation of 10,000 transactions, manual review required 22.2 hours. We need a system that automates the decision-making process while maintaining low latency and high accuracy.

## 2. Decision Drivers
1.  **Throughput Efficiency:** Must process high volumes of data without human bottlenecks.
2.  **Explainability:** Every automated action must be grounded in regulatory text (AML laws).
3.  **UI Resilience:** Avoid fragile UI-based automation in favor of industrial-grade API execution.

## 3. Proposed Solution: The Hybrid AI Funnel
We implemented a two-stage machine learning pipeline integrated with Agentic RPA:
1.  **Stage 1 - Isolation Forest (iForest):** Used for "Broad Sniffing." It processes 10,000 records in memory in ~5 seconds, clearing 95% of routine traffic almost instantly.
2.  **Stage 2 - Support Vector Machine (SVM):** Used for "Precision Interception." It executes high-dimensional hard-margin cuts on the remaining 5% of outliers (~10 seconds total).
3.  **Explainable AI (RAG):** When high risk is detected, a RAG module cross-references the features against an AML statute database, generating human-readable evidence (e.g., "AML Article 4").
4.  **API-First RPA:** UiPath bots bypass the UI and use `HTTP POST /api/lockBusiness` to trigger immediate asset freezes at the gateway level.

## 4. Consequences
* **155x Speed Improvement:** Total processing time dropped from 22.2 hours to 8.5 minutes for 10,000 records.
* **Audit Integrity:** Every block is justified by regulatory evidence rather than a "black-box" score.
* **Engineering Constraint:** Requires a high-quality vector database for the RAG component to remain accurate.
---

# ADR-002：实施基于非对称 ML 漏斗 (iForest + SVM) 的实时拦截架构

**状态：** 已接受
**日期：** 2026-03-05
**上下文：** `projects/02-Agentic-RPA-Compliance`

## 1. 背景
传统基于规则的 RPA 系统过于僵化，无法处理“蓝精灵”洗钱等复杂欺诈。它们会产生大量误报，并导致人工审查员产生认知疲劳。在我们的 10,000 条交易模拟中，人工审查需要 22.2 小时。我们需要一个能在保持低延迟和高准确性的同时，实现决策自动化的系统。

## 2. 决策驱动力
1.  **吞吐效率：** 必须在没有人工瓶颈的情况下处理海量数据。
2.  **可解释性：** 每一项自动化动作必须以监管文本（AML 法律）为依据。
3.  **UI 韧性：** 放弃脆弱的基于 UI 的自动化，转而采用工业级 API 执行。

## 3. 建议方案：混合 AI 漏斗
我们实施了一个与智能体 RPA 集成的两阶段机器学习流水线：
1.  **阶段 1 - 隔离森林 (iForest)：** 用于“广域嗅探”。它在约 5 秒内处理内存中的 10,000 条记录，几乎瞬间清空 95% 的常规流量。
2.  **阶段 2 - 支持向量机 (SVM)：** 用于“精准拦截”。它对剩余 5% 的异常数据执行高维硬边缘切割（总耗时约 10 秒）。
3.  **可解释 AI (RAG)：** 当检测到高风险时，RAG 模块将特征与反洗钱法规数据库进行交叉引用，生成人类可读的证据（如“反洗钱法第四条”）。
4.  **API 优先 RPA：** UiPath 机器人绕过 UI，使用 `HTTP POST /api/lockBusiness` 在网关层触发即时资产冻结。

## 4. 后果
* **155 倍速度提升：** 10,000 条记录的总处理时间从 22.2 小时下降到 8.5 分钟。
* **审计完整性：** 每一项拦截都有法规证据支持，而非“黑盒”分值。
* **工程约束：** 需要高质量的向量数据库以保持 RAG 组件的准确性。