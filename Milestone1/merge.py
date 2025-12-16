import pandas as pd

# Load files safely
sleep_df = pd.read_csv("/content/minuteSleep_merged.csv", low_memory=False)
steps_df = pd.read_csv("/content/minuteStepsNarrow_merged.csv", low_memory=False)
hr_df = pd.read_csv(
    "/content/heartrate_seconds_merged.csv",
    on_bad_lines="skip",
    low_memory=False
)

# Rename columns
sleep_df = sleep_df.rename(columns={"date": "Time", "value": "Sleep"})
steps_df = steps_df.rename(columns={"ActivityMinute": "Time"})
hr_df = hr_df.rename(columns={"Value": "HeartRate"})

# Fix datatypes
for df in [sleep_df, steps_df, hr_df]:
    df["Id"] = df["Id"].astype(str)

# Convert time
sleep_df["Time"] = pd.to_datetime(sleep_df["Time"], errors="coerce")
steps_df["Time"] = pd.to_datetime(steps_df["Time"], errors="coerce")
hr_df["Time"] = pd.to_datetime(hr_df["Time"], errors="coerce").dt.floor("min")

# Drop bad rows
sleep_df = sleep_df.dropna(subset=["Time"])
steps_df = steps_df.dropna(subset=["Time"])
hr_df = hr_df.dropna(subset=["Time"])

# AGGREGATE FIRST (THIS IS WHAT WAS MISSING)
steps_df = steps_df.groupby(
    ["Id", "Time"], as_index=False
)["Steps"].sum()

sleep_df = sleep_df.groupby(
    ["Id", "Time"], as_index=False
)["Sleep"].max()

hr_df = hr_df.groupby(
    ["Id", "Time"], as_index=False
)["HeartRate"].mean()

# NOW MERGE (ONE ROW PER MINUTE)
merged = steps_df.merge(
    sleep_df, on=["Id", "Time"], how="inner"
).merge(
    hr_df, on=["Id", "Time"], how="inner"
)

# Final cleanup
merged = merged.dropna().sort_values(["Id", "Time"])

# Save output
merged.to_csv("/content/fitbit_minute_OPTIMAL.csv", index=False)

print("FINAL OPTIMAL DATASET")
print("Shape:", merged.shape)
