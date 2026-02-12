# ==============================
# Milestone 1: Data Cleaning & Preprocessing
# Large Synthetic Dataset for EDA / ML (2 Lakh rows)
# ==============================

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# -------------------------------
# 1. PARAMETERS
# -------------------------------
num_rows = 200000  # 2,00,000 rows

countries = ["India", "USA", "Canada", "Australia", "UK", "Germany", "France"]
visa_types = ["Student", "Work", "Tourist", "Business"]

# -------------------------------
# 2. GENERATE SYNTHETIC DATA
# -------------------------------
app_ids = list(range(100001, 100001 + num_rows))

start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 12, 31)

# Random application dates
app_dates = [start_date + timedelta(days=random.randint(0, (end_date - start_date).days)) for _ in range(num_rows)]

# Decision date = app_date + random processing days (20 to 60)
decision_dates = [date + timedelta(days=random.randint(20, 60)) for date in app_dates]

# Random countries and visa types
country_col = [random.choice(countries) for _ in range(num_rows)]
visa_category_col = [random.choice(visa_types) for _ in range(num_rows)]

# Create DataFrame
df = pd.DataFrame({
    "app_id": app_ids,
    "app_date": app_dates,
    "decision_date": decision_dates,
    "country": country_col,
    "visa_category": visa_category_col
})

# -------------------------------
# 3. DATA CLEANING & PREPROCESSING
# -------------------------------
# Processing time in days
df["processing_time_days"] = (df["decision_date"] - df["app_date"]).dt.days

# Handle missing values (forward fill)
df.ffill(inplace=True)

# Delay status
df["delay_status"] = df["processing_time_days"].apply(
    lambda x: "High Delay" if x > 35 else "Normal Delay"
)

# Normalized processing time
df["normalized_time"] = (df["processing_time_days"] - np.mean(df["processing_time_days"])) / np.std(df["processing_time_days"])

# -------------------------------
# 4. BASIC STATISTICS
# -------------------------------
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])
print("Average processing time:", df["processing_time_days"].mean())
print("Maximum processing time:", df["processing_time_days"].max())

print("\nSample Data:")
print(df.head())

# -------------------------------
# 5. SAVE DATASET
# -------------------------------
df.to_csv("Visa_2Lakh_Dataset.csv", index=False)
print("\n✅ Large dataset saved as 'Visa_2Lakh_Dataset.csv'")
print("Number of rows in df:", len(df))


