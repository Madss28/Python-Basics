"""
BMI HEALTH ANALYZER
A comprehensive health assessment tool.
Demonstrates: functions, conditionals, data validation, health metrics
"""

def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI).
    
    Formula: weight (kg) / height (m)²
    
    Args:
        weight_kg (float): Weight in kilograms
        height_m (float): Height in meters
    
    Returns:
        float: BMI value
    
    Example:
        >>> calculate_bmi(70, 1.75)
        22.86
    """
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Weight and height must be positive")
    return weight_kg / (height_m ** 2)


def get_bmi_category(bmi):
    """
    Determine BMI category based on WHO standards.
    
    Args:
        bmi (float): BMI value
    
    Returns:
        str: BMI category
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def get_health_risk(bmi):
    """
    Assess health risk based on BMI.
    
    Args:
        bmi (float): BMI value
    
    Returns:
        str: Health risk level
    """
    if bmi < 18.5:
        return "Increased risk of nutritional deficiency"
    elif bmi < 25:
        return "Low risk"
    elif bmi < 30:
        return "Moderate risk of weight-related issues"
    else:
        return "High risk of obesity-related conditions"


def calculate_bmr(weight_kg, height_m, age, gender):
    """
    Calculate Basal Metabolic Rate using Mifflin-St Jeor equation.
    
    BMR = calories burned at rest.
    
    Args:
        weight_kg (float): Weight in kilograms
        height_m (float): Height in meters
        age (int): Age in years
        gender (str): 'M' or 'F'
    
    Returns:
        int: BMR in calories per day
    """
    height_cm = height_m * 100
    
    if gender.upper() == 'M':
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
    else:
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161
    
    return int(bmr)


def get_ideal_weight_range(height_m):
    """
    Calculate ideal weight range using BMI 18.5-24.9.
    
    Args:
        height_m (float): Height in meters
    
    Returns:
        tuple: (min_weight, max_weight) in kg
    """
    min_weight = 18.5 * (height_m ** 2)
    max_weight = 24.9 * (height_m ** 2)
    return (round(min_weight, 1), round(max_weight, 1))


def main():
    """Main program with user interaction."""
    print("\n" + "=" * 60)
    print("           HEALTH ASSESSMENT TOOL")
    print("           Biomedical Data Analysis")
    print("=" * 60)
    
    print("\n📋 Please enter your details:")
    print("-" * 40)
    
    try:
        name = input("Full name: ")
        age = int(input("Age (years): "))
        gender = input("Gender (M/F): ").upper()
        weight = float(input("Weight (kg): "))
        height = float(input("Height (m): "))
        
        # Validate inputs
        if age <= 0 or age > 120:
            print("❌ Invalid age. Please enter a valid age.")
            return
        if weight <= 0 or weight > 500:
            print("❌ Invalid weight. Please enter a valid weight.")
            return
        if height <= 0 or height > 3:
            print("❌ Invalid height. Please enter a valid height.")
            return
        
        # Perform calculations
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        risk = get_health_risk(bmi)
        bmr = calculate_bmr(weight, height, age, gender)
        ideal_range = get_ideal_weight_range(height)
        
        # Display results
        print("\n" + "=" * 60)
        print(f"           HEALTH REPORT FOR {name.upper()}")
        print("=" * 60)
        
        print(f"\n📊 BASIC METRICS:")
        print(f"   • Age: {age} years")
        print(f"   • Gender: {gender}")
        print(f"   • Weight: {weight} kg")
        print(f"   • Height: {height} m")
        
        print(f"\n📈 BMI ANALYSIS:")
        print(f"   • BMI: {bmi:.1f}")
        print(f"   • Category: {category}")
        print(f"   • Health Risk: {risk}")
        
        print(f"\n🔥 METABOLIC ANALYSIS:")
        print(f"   • BMR: {bmr} calories/day")
        print(f"   • Ideal weight range: {ideal_range[0]} - {ideal_range[1]} kg")
        
        print("\n" + "=" * 60)
        print("           REPORT COMPLETE")
        print("=" * 60)
        print("\n💡 Note: This is for informational purposes only.")
        print("   Consult a healthcare professional for medical advice.")
        
    except ValueError:
        print("\n❌ Error: Please enter valid numbers for age, weight, and height.")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")


if __name__ == "__main__":
    main()
