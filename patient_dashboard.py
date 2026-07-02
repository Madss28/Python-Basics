"""
PATIENT HEALTH DASHBOARD
Complete healthcare data analysis with visualizations
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("=" * 50)
print("PATIENT HEALTH DASHBOARD")
print("=" * 50)

# ============================================
# PART 1: CREATE PATIENT DATA
# ============================================
print("\n1. CREATING PATIENT DATA...")

np.random.seed(42)

data = {
    "Patient_ID": range(101, 131),
    "Name": [f"Patient_{i}" for i in range(1, 31)],
    "Age": np.random.randint(18, 80, 30),
    "Gender": np.random.choice(["M", "F"], 30),
    "Heart_Rate": np.random.randint(60, 110, 30),
    "Blood_Pressure_Sys": np.random.randint(110, 160, 30),
    "Blood_Pressure_Dia": np.random.randint(70, 100, 30),
    "Diagnosis": np.random.choice(
        ["Healthy", "Flu", "Hypertension", "Heart Disease"],
        size=30,
        p=[0.35, 0.25, 0.25, 0.15]
    )
}

df = pd.DataFrame(data)
print("✅ Patient data created!")

# ============================================
# PART 2: EXPLORE DATA
# ============================================
print("\n2. EXPLORING DATA...")

print(f"Total patients: {len(df)}")
print(f"Columns: {df.columns.tolist()}")
print(f"\nFirst 5 patients:")
print(df.head())

print(f"\nData statistics:")
print(df.describe())

# ============================================
# PART 3: DATA CLEANING
# ============================================
print("\n3. CLEANING DATA...")

# Check for missing values
print("Missing values:")
print(df.isnull().sum())

# Add BMI (Body Mass Index)
df["Weight"] = np.random.uniform(50, 100, 30)
df["Height"] = np.random.uniform(1.5, 1.9, 30)
df["BMI"] = df["Weight"] / (df["Height"] ** 2)

# Categorize BMI
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

df["BMI_Category"] = df["BMI"].apply(bmi_category)

# Categorize Blood Pressure
def bp_category(systolic):
    if systolic < 120:
        return "Normal"
    elif systolic < 140:
        return "Elevated"
    else:
        return "High"

df["BP_Category"] = df["Blood_Pressure_Sys"].apply(bp_category)

# Categorize Heart Rate
def hr_category(hr):
    if hr < 60:
        return "Low"
    elif hr <= 100:
        return "Normal"
    else:
        return "High"

df["HR_Category"] = df["Heart_Rate"].apply(hr_category)

print("✅ Cleaned and added new columns!")

# ============================================
# PART 4: ANALYSIS
# ============================================
print("\n4. ANALYZING DATA...")

# Average age by diagnosis
print("\nAverage age by diagnosis:")
print(df.groupby("Diagnosis")["Age"].mean().round(1))

# Average heart rate by diagnosis
print("\nAverage heart rate by diagnosis:")
print(df.groupby("Diagnosis")["Heart_Rate"].mean().round(1))

# Count by diagnosis
print("\nPatient count by diagnosis:")
print(df["Diagnosis"].value_counts())

# Count by BMI category
print("\nPatient count by BMI category:")
print(df["BMI_Category"].value_counts())

# Count by Blood Pressure category
print("\nPatient count by BP category:")
print(df["BP_Category"].value_counts())

# High risk patients (Age > 50 and Heart_Rate > 90)
high_risk = df[(df["Age"] > 50) & (df["Heart_Rate"] > 90)]
print(f"\nHigh risk patients: {len(high_risk)}")
print(high_risk[["Name", "Age", "Heart_Rate", "Diagnosis"]])

# ============================================
# PART 5: VISUALIZATIONS
# ============================================
print("\n5. CREATING VISUALIZATIONS...")

# Create a figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Patient Health Dashboard", fontsize=16, fontweight="bold")

# Plot 1: Diagnosis distribution
ax1 = axes[0, 0]
diagnosis_counts = df["Diagnosis"].value_counts()
ax1.bar(diagnosis_counts.index, diagnosis_counts.values, color="skyblue")
ax1.set_title("Patients by Diagnosis")
ax1.set_xlabel("Diagnosis")
ax1.set_ylabel("Number of Patients")

# Plot 2: Age distribution
ax2 = axes[0, 1]
ax2.hist(df["Age"], bins=10, color="lightgreen", edgecolor="black")
ax2.set_title("Age Distribution")
ax2.set_xlabel("Age")
ax2.set_ylabel("Number of Patients")

# Plot 3: Average heart rate by diagnosis
ax3 = axes[1, 0]
avg_hr = df.groupby("Diagnosis")["Heart_Rate"].mean()
ax3.bar(avg_hr.index, avg_hr.values, color="coral")
ax3.set_title("Average Heart Rate by Diagnosis")
ax3.set_xlabel("Diagnosis")
ax3.set_ylabel("Heart Rate (bpm)")

# Plot 4: BMI distribution
ax4 = axes[1, 1]
bmi_categories = df["BMI_Category"].value_counts()
ax4.bar(bmi_categories.index, bmi_categories.values, color="lightblue")
ax4.set_title("BMI Distribution")
ax4.set_xlabel("BMI Category")
ax4.set_ylabel("Number of Patients")

plt.tight_layout()
plt.savefig("patient_dashboard.png")
print("✅ Dashboard saved as 'patient_dashboard.png'")

# ============================================
# PART 6: SUMMARY REPORT
# ============================================
print("\n6. GENERATING SUMMARY REPORT...")

# Create summary report
summary = {
    "Total Patients": len(df),
    "Average Age": round(df["Age"].mean(), 1),
    "Average Heart Rate": round(df["Heart_Rate"].mean(), 1),
    "Average BMI": round(df["BMI"].mean(), 1),
    "Most Common Diagnosis": df["Diagnosis"].mode().iloc[0],
    "Most Common BMI Category": df["BMI_Category"].mode().iloc[0],
    "Most Common BP Category": df["BP_Category"].mode().iloc[0],
    "High Risk Patients": len(high_risk)
}

print("\nPATIENT SUMMARY:")
for key, value in summary.items():
    print(f"  {key}: {value}")

# ============================================
# PART 7: SAVE RESULTS
# ============================================
print("\n7. SAVING RESULTS...")

# Save clean data
df.to_csv("patient_dashboard_data.csv", index=False)
print("✅ Clean data saved to 'patient_dashboard_data.csv'")

# Save summary
df.to_excel("patient_dashboard.xlsx", index=False)
print("✅ Excel file saved to 'patient_dashboard.xlsx'")

# Save high risk patients
high_risk.to_csv("high_risk_patients.csv", index=False)
print("✅ High risk patients saved to 'high_risk_patients.csv'")

print("\n" + "=" * 50)
print("✅ PATIENT DASHBOARD COMPLETE")
print("=" * 50)
