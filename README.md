# Azure Cloud Journey: Engineering the AI-Native Future

This repository documents my transition from a **10-year Front-end Veteran** to an **Enterprise AI Cloud Architect**. It stores verified, high-availability, and low-latency Cloud-Native Proof of Concepts (PoC).

[中文版说明](./README_CN.md)

## 🎯 Strategic Roadmap (2025-2026)
* **Phase 1:** Master Azure AI & Data Engineering loop. Target Certs: `AI-102`, `AZ-305`.
* **Phase 2:** Deployment in Singapore. Focus on High-Concurrency FinTech & RAG Architectures.

## 🏗 Featured Projects

### 01. Low-Latency Fraud Interception API
* **Problem:** Beating the 50ms core banking gateway timeout.
* **Performance:** 22ms E2E Latency / 92.86% Recall.
* **Stack:** Azure Functions, APIM, XGBoost.
* **[View Project Details](./projects/01-Fraud-Interception-API/)**

### 02. RAG-Driven Agentic RPA Compliance Gateway
* **Problem:** Semantic blindness and severe cognitive fatigue in rule-based Anti-Money Laundering (AML) operations.
* **Performance:** 155x throughput increase (processed 10,000 transaction vectors in 8.5 minutes).
* **Stack:** UiPath (API-First Execution), iForest + SVM (Asymmetric ML Funnel), RAG Vector Store (Explainable AI).
* **[View Project Details](./projects/02-Agentic-RPA-Compliance/)**

## 🧠 Architecture Decision Records (ADRs)
We don't guess. We measure.
* [ADR-001: Bypassing RPA GUI for API-First Real-Time Interception](./ADRs/ADR-001-Fraud-API-API-First.md)
* [ADR-002: Implementation of Asymmetric ML Funnel (iForest + SVM) for Real-time Interception](./ADRs/ADR-002-RAG-Driven-Agentic-RPA.md)

---
"In Cloud Architecture, the only truth is the latency log."