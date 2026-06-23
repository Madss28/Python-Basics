"""
DATA CLEANING PRACTICE
Handling messy data with Pandas.
"""

import pandas as pd
import numpy as np

# Create messy data
data = {
    "Name": ["John", "Sarah", "Mike", "Emma", "James", "Lisa"],
    "Age": [45, 32, "twenty-eight", 55, None, 35],
    "Heart_Rate": [72, 68, 75, "eighty", 65, 70],
    "Diagnosis": ["Flu", "Healthy", "Healthy", "Hypertension", "Healthy", None]
}

df = pd.DataFrame(data)

print("=== ORIGINAL DATA ===")
print(df)

print("\n=== DATA INFO ===")
print(df.info())

# Clean the data
print("\n=== CLEANING PROCESS ===")

# 1. Fix Age column (convert to numeric, replace errors)
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
print("1. Fixed Age column (coerced errors to NaN)")

# 2. Fix Heart_Rate column
df["Heart_Rate"] = pd.to_numeric(df["Heart_Rate"], errors="coerce")
print("2. Fixed Heart_Rate column")

# 3. Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Heart_Rate"] = df["Heart_Rate"].fillna(df["Heart_Rate"].mean())
df["Diagnosis"] = df["Diagnosis"].fillna("Unknown")
print("3. Filled missing values")

print("\n=== CLEANED DATA ===")
print(df)

# Save cleaned data
df.to_csv("cleaned_patient_data.csv", index=False)
print("\n✅ Cleaned data saved to cleaned_patient_data.csv")
