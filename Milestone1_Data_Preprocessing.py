import pandas as pd
import numpy as np

# Create synthetic visa dataset
visa_records = {
    "app_id": [101, 102, 103, 104],
    "app_date": ["2024-01-05", "2024-02-10", "2024-03-01", "2024-03-20"],
    "decision_date": ["2024-02-08", "2024-03-18", "2024-04-10", "2024-04-25"],
    "country": ["India", "Canada", "USA", "Australia"],
    "visa_category": ["Student", "Work", "Tourist", "Student"]
}

df = pd.DataFrame(visa_records)

# Convert date columns
df["app_date"] = pd.to_datetime(df["app_date"])
df["decision_date"] = pd.to_datetime(df["decision_date"])

# Calculate processing time
df["processing_time_days"] = (df["decision_date"] - df["app_date"]).dt.days

# Handle missing values (if any)
df.ffill(inplace=True)


# Basic statistics
print("Average processing time:", df["processing_time_days"].mean())
print("Maximum processing time:", df["processing_time_days"].max())

# Create delay category
df["delay_status"] = df["processing_time_days"].apply(
    lambda x: "High Delay" if x > 35 else "Normal Delay"
)

# Normalize processing time
df["normalized_time"] = (
    (df["processing_time_days"] - np.mean(df["processing_time_days"])) /
    np.std(df["processing_time_days"])
)

print(df)
