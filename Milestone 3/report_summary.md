#  FitPulse: Health Anomaly Detection System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Milestone%203%20Complete-success?style=for-the-badge)
![Libraries](https://img.shields.io/badge/Libraries-Prophet%20%7C%20Scikit--Learn%20%7C%20TSFresh-orange?style=for-the-badge)

---

##  Project Overview

**FitPulse** is an intelligent health anomaly detection system built on time-series data from fitness wearables such as **Fitbit** and **Apple Watch**.

Unlike traditional fitness apps that rely on **static thresholds** (e.g., *HR > 100 BPM*), FitPulse introduces a **context-aware, multi-layered detection engine** capable of identifying early health risks by understanding *user behavior, trends, and medical constraints* simultaneously.

At its core lies a **Triple-Filter Detection Architecture** that answers:

- *Is this normal for this specific user?*
- *Was this value expected based on historical trends?*
- *Is this value medically unsafe?*

---

##  Triple-Filter Detection Architecture

| Filter | Purpose | Description |
|------|--------|------------|
| **Filter A — Statistical** | Trend Deviations | Uses **Facebook Prophet** to flag points outside confidence intervals |
| **Filter B — Medical** | Safety Constraints | Applies medical domain rules (e.g., tachycardia detection) |
| **Filter C — Contextual** | Behavioral Validation | Cross-checks activity & sleep context to reduce false positives |

> An anomaly is confirmed only when one or more filters agree, improving reliability and explainability.

---

##  Key Features & Milestones

###  Milestone 2: Intelligent Modeling
-  **Automated Feature Engineering** using **TSFresh**  
  (skewness, kurtosis, energy, entropy, etc.)
-  **User Persona Clustering** with **K-Means** and **DBSCAN**  
  (e.g., *Sedentary*, *Active*, *High-Intensity Athlete*)
-  **Dimensionality Reduction** using **PCA** for behavior visualization

---

###  Milestone 3: Anomaly Detection Engine
- **Time-Series Forecasting** using **Facebook Prophet**
-  **Statistical Anomaly Detection** (99% confidence bounds)
-  **Medical Rule Enforcement**
  - High HR while sedentary
  - Sleep deprivation risk amplification
-  **Context-Aware Filtering**
  - Differentiates between *exercise-induced* and *rest-time* anomalies
-  **Root Cause Tagging**
  - Generates explainable anomaly reasons:
    ```
    Trend Spike + High HR at Rest + Critical Sleep Deprivation + Compound Risk
    ```

---

## Tech Stack

| Category | Tools |
|--------|------|
| **Language** | Python 3.10+ |
| **Data Processing** | Pandas, NumPy |
| **Time-Series Forecasting** | Facebook Prophet |
| **Machine Learning** | Scikit-Learn, TSFresh |
| **Visualization** | Plotly, Matplotlib |
| **Environment** | Google Colab / Jupyter |

