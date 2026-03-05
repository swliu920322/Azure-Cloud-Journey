# Low-Latency Fraud Prevention API (Azure-Native Architecture)

## 🏗 Architectural Overview
This repository contains the physical execution layer for a high-frequency financial fraud interception engine. It bypasses fragile GUI-based RPA systems, directly wiring an XGBoost predictive model to an **Azure Serverless (Function App)** backend.

By explicitly forcing the API routing matrix, the system neutralizes unauthorized financial payloads before the standard **50ms core banking gateway timeout**.

### ⚡ Performance Benchmarks (Proof of Concept)
* **Inference Engine:** XGBoost (Constrained via Taylor Expansion Gain, `max_depth=6`)
* **Critical Freeze Threshold:** `P(Y=1|X) >= 0.90`
* **MFA Verification Friction:** `2.89%` of legitimate traffic
* **Execution Latency:** Clocked at **22ms** on Azure Consumption Plan (Target P95: 17.44ms on Premium Tier).

![Azure API 压测实证](assets/delay.png)

## ⚙️ Repository Structure
* `train_pipeline.py`: Executes data ingestion, SMOTE topological rewriting, and exports the serialized `.json` model.
* `inference_api.py`: The stateless Azure Function handler. Loads the model in the global namespace to eliminate cold-start penalties during high-throughput bursts.
* `config.yaml`: Centralized control plane for hyperparameters and routing thresholds.

## 🚀 Deployment (Azure)
This pipeline is designed to be deployed directly to Azure Functions and fronted by Azure API Management (APIM) for rate-limiting and JWT authentication.