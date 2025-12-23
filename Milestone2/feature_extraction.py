import pandas as pd
import numpy as np
from scipy.stats import kurtosis, skew

from tsfresh import extract_features
from tsfresh.utilities.dataframe_functions import impute
from tsfresh.feature_extraction import EfficientFCParameters

from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import VarianceThreshold


# --------------------------------------------------
# Load and preprocess dataset
# --------------------------------------------------
def load_and_preprocess_data(csv_path):
    df = pd.read_csv(csv_path)

    # standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # convert timestamp
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # sort by person and time
    df = df.sort_values(['person_id', 'timestamp']).reset_index(drop=True)

    return df


# --------------------------------------------------
# Encode categorical columns
# --------------------------------------------------
def encode_categorical_features(df, categorical_cols):
    df_encoded = df.copy()
    encoder = LabelEncoder()

    for col in categorical_cols:
        df_encoded[col] = encoder.fit_transform(df_encoded[col].astype(str))

    return df_encoded


# --------------------------------------------------
# Statistical features per person
# --------------------------------------------------
def extract_statistical_features(df, ts_cols):
    rows = []

    for pid, group in df.groupby('person_id'):
        row = {'person_id': pid}

        for col in ts_cols:
            row[f'{col}_mean'] = group[col].mean()
            row[f'{col}_std'] = group[col].std()
            row[f'{col}_kurtosis'] = kurtosis(group[col])
            row[f'{col}_skewness'] = skew(group[col])

        rows.append(row)

    return pd.DataFrame(rows)


# --------------------------------------------------
# TSFresh feature extraction (includes frequency features)
# --------------------------------------------------
def extract_tsfresh_features(df, ts_cols):
    tsfresh_input = df[['person_id', 'timestamp'] + ts_cols]

    features = extract_features(
        tsfresh_input,
        column_id='person_id',
        column_sort='timestamp',
        default_fc_parameters=EfficientFCParameters(),
        n_jobs=0
    )

    impute(features)
    return features


# --------------------------------------------------
# Feature selection using variance threshold
# --------------------------------------------------
def select_relevant_features(features, threshold=0.01):
    if features.shape[0] <= 1:
        # variance selection not possible with single sample
        selected_cols = features.columns
    else:
        selector = VarianceThreshold(threshold=threshold)
        selector.fit(features)
        selected_cols = features.columns[selector.get_support()]

    return selected_cols


# --------------------------------------------------
# Build final feature matrix
# --------------------------------------------------
def build_feature_matrix(
    stat_features,
    tsfresh_features,
    selected_cols,
    meta_features
):
    tsfresh_reset = tsfresh_features[selected_cols].reset_index()
    tsfresh_reset = tsfresh_reset.rename(columns={'index': 'person_id'})

    X = (
        stat_features
        .merge(tsfresh_reset, on='person_id', how='inner')
        .merge(meta_features, on='person_id', how='inner')
    )

    X = X.drop(columns=['person_id']).fillna(0)
    return X
