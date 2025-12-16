# FitPulse: Health Anomaly Detection from Fitness Devices

## 📌 Project Overview
**FitPulse** is a health analytics project focused on detecting physiological anomalies using wearable fitness device data.  
This repository contains **Milestone 1**, which establishes a **robust data preprocessing pipeline** for raw Fitbit logs, preparing them for downstream analytics and anomaly detection models.

---

## 🎯 Milestone 1 Objective
The primary goal of this milestone is to:
- Ingest raw Fitbit CSV data
- Normalize timestamps to a unified UTC format
- Handle missing and misaligned values
- Align all health metrics to a **1-minute time resolution**

This preprocessing step ensures data consistency and reliability for future machine learning models.

---

## 📂 Dataset Source
**Source:** Public Fitbit Fitness Tracker Dataset  

### Files Used
| File Name | Description |
|---------|------------|
| `heartrate_seconds_merged.csv` | Heart rate values recorded per second |
| `minuteStepsNarrow_merged.csv` | Step counts aggregated per minute |
| `minuteSleep_merged.csv` | Sleep stage logs |

---

## 🔄 Data Processing Pipeline

### 1️⃣ Data Ingestion
- Loaded raw CSV files using **Pandas**
- Validated schema consistency and column integrity

### 2️⃣ Time Normalization
- Converted timestamp columns to `datetime`
- Standardized all timestamps to **UTC**
- Ensured uniform time formatting across datasets

### 3️⃣ Resampling & Alignment
- Aggregated heart rate data from **seconds → 1-minute mean**
- Aggregated step counts using **1-minute sum**
- Aligned sleep logs to the same 1-minute timeline

### 4️⃣ Missing Value Handling
- Identified gaps caused by device inactivity or logging issues
- Applied forward-fill and safe imputation strategies where applicable

### 6️⃣ Output Generation
- Exported the final cleaned dataset as:
