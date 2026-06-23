"""
FUNCTION PRACTICE
Reusable functions for common tasks.
"""

def greet_user(name):
    """Say hello to a user"""
    return f"Hello, {name}! Welcome back."

def calculate_bmi(weight, height):
    """Calculate BMI from weight (kg) and height (m)"""
    return weight / (height ** 2)

def categorize_bmi(bmi):
    """Categorize BMI value"""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def get_patient_summary(name, weight, height):
    """Generate a complete patient summary"""
    bmi = calculate_bmi(weight, height)
    category = categorize_bmi(bmi)
    return f"""
    Patient: {name}
    Weight: {weight} kg
    Height: {height} m
    BMI: {bmi:.1f} ({category})
    """

# Test the functions
print("=== FUNCTION PRACTICE ===\n")

print(greet_user("Madhurima"))

summary = get_patient_summary("John", 85, 1.75)
print(summary)

summary = get_patient_summary("Sarah", 65, 1.65)
print(summary)

print("✅ Functions are working!")
