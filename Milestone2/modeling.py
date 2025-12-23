import matplotlib.pyplot as plt
import seaborn as sns

from prophet import Prophet
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, DBSCAN


# --------------------------------------------------
# Prophet trend modeling and residual computation
# --------------------------------------------------
def run_prophet_trend(df, column, forecast_days=30):
    data = df[['timestamp', column]].rename(
        columns={'timestamp': 'ds', column: 'y'}
    )

    model = Prophet(
        daily_seasonality=True,
        weekly_seasonality=True,
        yearly_seasonality=False
    )

    model.fit(data)

    future = model.make_future_dataframe(periods=forecast_days)
    forecast = model.predict(future)

    # Plot trend with confidence intervals
    model.plot(forecast)
    plt.title(f"{column.replace('_', ' ').title()} Trend & Forecast")
    plt.show()

    # Compute residuals
    residuals = data['y'].values - forecast.loc[:len(data)-1, 'yhat'].values

    return forecast, residuals


# --------------------------------------------------
# Dimensionality reduction using PCA
# --------------------------------------------------
def reduce_dimensions(features, n_components=2):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(features)

    pca = PCA(n_components=n_components, random_state=42)
    X_pca = pca.fit_transform(X_scaled)

    return X_pca, pca.explained_variance_ratio_


# --------------------------------------------------
# KMeans clustering
# --------------------------------------------------
def apply_kmeans(X_pca, n_clusters=3):
    kmeans = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )
    labels = kmeans.fit_predict(X_pca)
    return labels


# --------------------------------------------------
# DBSCAN clustering (for atypical behavior)
# --------------------------------------------------
def apply_dbscan(X_pca, eps=0.6, min_samples=3):
    dbscan = DBSCAN(
        eps=eps,
        min_samples=min_samples
    )
    labels = dbscan.fit_predict(X_pca)
    return labels


# --------------------------------------------------
# Cluster visualization
# --------------------------------------------------
def visualize_clusters(X_pca, labels, title):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        x=X_pca[:, 0],
        y=X_pca[:, 1],
        hue=labels,
        palette='Set2'
    )
    plt.title(title)
    plt.xlabel("PCA Component 1")
    plt.ylabel("PCA Component 2")
    plt.show()
