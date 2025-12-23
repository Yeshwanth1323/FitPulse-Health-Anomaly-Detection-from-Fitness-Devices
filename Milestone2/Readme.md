# FitPulse: Health Anomaly Detection from Fitness Devices

##  Project Overview
**FitPulse** is a health analytics project focused on detecting physiological anomalies using wearable fitness device data.  
This repository contains **Milestone 1**, which establishes a **robust data preprocessing pipeline** for raw Fitbit logs, preparing them for downstream analytics and anomaly detection models.

https://colab.research.google.com/drive/10EF3-1CxkJCdDc94-KZCmj30pUqBsAi5?usp=sharing

## Milestone 2: Feature Engineering, Trend Modeling & Behavioral Analysis

---

##  Overview
Milestone 2 focuses on extracting meaningful insights from preprocessed fitness data through advanced feature engineering, temporal trend modeling, and behavioral pattern analysis. This milestone establishes a strong analytical foundation for detecting health anomalies in subsequent stages.

---

## Objective
The objectives of this milestone are:
- To extract robust statistical and time-series features from fitness device data
- To model seasonal and temporal trends in health metrics
- To identify behavioral patterns and deviations using unsupervised learning techniques

---

## Dataset Description
The dataset contains time-stamped fitness and lifestyle data collected from wearable devices. Each record corresponds to an individual and includes physiological, activity-based, sleep-related, and demographic attributes.

### Key Features:
- Heart Rate
- Daily Steps
- Sleep Duration and Quality
- Blood Pressure (Systolic and Diastolic)
- Physical Activity Level
- Stress Level
- BMI Category
- Demographic Information
- Timestamp

---

##  Feature Engineering

### Statistical Feature Extraction
Descriptive statistical features such as mean, standard deviation, skewness, and kurtosis are computed for heart rate, daily steps, and sleep duration on a per-user basis. These features summarize individual health behavior over time.

### Automated Time-Series Feature Extraction (TSFresh)
TSFresh is used to automatically extract advanced time-series features, including frequency-domain characteristics, autocorrelation, and entropy-based features. This enables capturing complex temporal patterns without manual feature design.

### Feature Selection
Variance Thresholding is applied to remove low-variance and non-informative features, reducing dimensionality and improving clustering performance.

---

## Trend Modeling and Forecasting

### Prophet-Based Trend Modeling
Facebook Prophet is used to model seasonal and temporal trends in heart rate, daily steps, and sleep duration. Prophet effectively handles missing data and captures daily and weekly seasonality.

### Residual Analysis
Forecasted values are compared with actual observations to compute residuals. Significant deviations from expected trends indicate potential unusual or anomalous behavior.

### Visualization
Each metric is visualized with confidence intervals to provide clear insights into trends, seasonal patterns, and deviations.


## Behavioral Pattern Analysis

### Dimensionality Reduction
Principal Component Analysis (PCA) is applied to reduce the high-dimensional feature space to two components, enabling efficient visualization and clustering.

### Clustering Techniques
- KMeans clustering is used to group individuals with similar health and activity patterns.
- DBSCAN is used to identify atypical or isolated behavioral patterns that may represent abnormal behavior.

### Cluster Interpretation
Clusters represent different lifestyle and health behavior profiles, while noise points or isolated clusters often indicate deviations from normal patterns.

---

##  Tools and Libraries Used
- Python
- Pandas, NumPy, SciPy
- TSFresh
- Facebook Prophet
- Scikit-learn
- Matplotlib, Seaborn
- Google Colaborator


##  Visual Outputs
This milestone includes:
- Trend and forecast plots with confidence intervals
- PCA-based cluster visualizations
- Residual plots for anomaly indication

<img width="701" height="539" alt="image" src="https://github.com/user-attachments/assets/86a9b99b-2221-4e3a-8fd0-338b26799977" />



