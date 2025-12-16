import pandas as pd

# =========================================================
# STEP 1: Load dataset and validate schema
# ---------------------------------------------------------
# This step ensures the input file exists and contains
# all the required columns needed for further processing.
# =========================================================

def load_and_validate(filepath):
    df = pd.read_csv(filepath, low_memory=False)

    required_cols = {"Id", "Time", "Steps", "Sleep", "HeartRate"}
    if not required_cols.issubset(df.columns):
        raise ValueError("Invalid schema: Missing required columns")

    return df


# =========================================================
# STEP 2: Normalize timestamps to UTC
# ---------------------------------------------------------
# Converts the Time column to pandas datetime format,
# enforces UTC timezone, and removes invalid timestamps.
# =========================================================

def normalize_timestamps(df):
    df["Time"] = pd.to_datetime(df["Time"], errors="coerce", utc=True)
    df = df.dropna(subset=["Time"])
    return df


# =========================================================
# STEP 3: Clean and standardize data types
# ---------------------------------------------------------
# Ensures IDs are treated as strings and all numeric
# sensor values are converted to numeric format safely.
# =========================================================

def clean_dtypes(df):
    df["Id"] = df["Id"].astype(str)
    df["Steps"] = pd.to_numeric(df["Steps"], errors="coerce")
    df["Sleep"] = pd.to_numeric(df["Sleep"], errors="coerce")
    df["HeartRate"] = pd.to_numeric(df["HeartRate"], errors="coerce")
    return df


# =========================================================
# STEP 4: Handle missing and null values
# ---------------------------------------------------------
# Uses domain-aware strategies:
# - Steps: 0 indicates no movement
# - Sleep: 0 indicates awake state
# - HeartRate: median value avoids outlier bias
# =========================================================

def handle_missing_values(df):
    df["Steps"] = df["Steps"].fillna(0)
    df["Sleep"] = df["Sleep"].fillna(0)
    df["HeartRate"] = df["HeartRate"].fillna(df["HeartRate"].median())
    return df


# =========================================================
# STEP 5: Align all metrics to a 1-minute interval
# ---------------------------------------------------------
# Aggregates multiple records within the same minute:
# - Steps summed
# - Sleep state preserved using max
# - Heart rate averaged
# =========================================================

def align_to_minute(df):
    df = (
        df.set_index("Time")
          .groupby("Id")
          .resample("1min")
          .agg({
              "Steps": "sum",
              "Sleep": "max",
              "HeartRate": "mean"
          })
          .reset_index()
    )
    return df


# =========================================================
# STEP 6: Final cleanup and ordering
# ---------------------------------------------------------
# Removes any remaining nulls and sorts the dataset
# by user ID and timestamp for consistency.
# =========================================================

def final_cleanup(df):
    df = df.dropna()
    df = df.sort_values(["Id", "Time"])
    return df


# =========================================================
# MAIN EXECUTION PIPELINE
# =========================================================

df = load_and_validate("/content/fitbit_minute_OPTIMAL.csv")
df = normalize_timestamps(df)
df = clean_dtypes(df)
df = handle_missing_values(df)
df = align_to_minute(df)
df = final_cleanup(df)

# Save the final cleaned dataset
df.to_csv("/content/fitbit_clean_final.csv", index=False)

print("✅ Preprocessing completed successfully")
print("Final dataset shape:", df.shape)
