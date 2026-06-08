"""
HEART RATE MONITOR
Clinical heart rate analysis tool.
Demonstrates: functions, lists, statistics, medical reference ranges
"""

def classify_heart_rate(bpm, age=None):
    """
    Classify heart rate based on medical standards.
    
    Normal adult range: 60-100 bpm
    Athletes can be lower (40-60)
    
    Args:
        bpm (int): Heart rate in beats per minute
        age (int, optional): Age in years
    
    Returns:
        str: Classification (Low, Normal, High)
    """
    if age and age < 18:
        # Pediatric ranges
        if bpm < 70:
            return "Low for age"
        elif bpm <= 100:
            return "Normal for age"
        else:
            return "High for age"
    else:
        # Adult ranges
        if bpm < 60:
            return "Bradycardia (Low)"
        elif bpm <= 100:
            return "Normal"
        else:
            return "Tachycardia (High)"


def get_medical_advice(bpm, classification):
    """
    Provide medical advice based on heart rate.
    
    Args:
        bpm (int): Heart rate value
        classification (str): Classification from classify_heart_rate
    
    Returns:
        str: Medical advice
    """
    if "Low" in classification:
        if bpm < 50:
            return "⚠️ Seek medical evaluation if symptomatic (fatigue, dizziness)"
        else:
            return "✓ Monitor. Common in athletes. Consult if concerned."
    elif "Normal" in classification:
        return "✓ Heart rate within normal range."
    else:  # High
        if bpm > 120:
            return "⚠️ Seek medical attention if persistent or伴有 symptoms"
        else:
            return "✓ Rest and re-measure. Avoid caffeine/stress before retesting."


def calculate_heart_rate_zone(bpm, age):
    """
    Calculate training zone based on maximum heart rate.
    Max HR = 220 - age
    
    Args:
        bpm (int): Current heart rate
        age (int): Age in years
    
    Returns:
        str: Training zone
    """
    max_hr = 220 - age
    percentage = (bpm / max_hr) * 100
    
    if percentage < 50:
        return "Very Light (Recovery Zone)"
    elif percentage < 60:
        return "Light (Fat Burn Zone)"
    elif percentage < 70:
        return "Moderate (Cardio Zone)"
    elif percentage < 85:
        return "Vigorous (Peak Zone)"
    else:
        return "Maximum (Red Line Zone)"


def analyze_multiple_readings(readings):
    """
    Analyze multiple heart rate readings.
    
    Args:
        readings (list): List of heart rate values
    
    Returns:
        dict: Statistical summary
    """
    if not readings:
        return {"error": "No readings provided"}
    
    return {
        "average": sum(readings) / len(readings),
        "min": min(readings),
        "max": max(readings),
        "range": max(readings) - min(readings),
        "count": len(readings),
        "resting_estimate": min(readings)  # Approximate resting HR
    }


def main():
    """Main program."""
    print("\n" + "=" * 50)
    print("      HEART RATE CLINICAL ANALYZER")
    print("=" * 50)
    
    print("\n📋 Patient Information")
    print("-" * 30)
    
    name = input("Patient name: ")
    age = int(input("Age: "))
    heart_rate = int(input("Current heart rate (bpm): "))
    
    # Classify
    classification = classify_heart_rate(heart_rate, age)
    advice = get_medical_advice(heart_rate, classification)
    training_zone = calculate_heart_rate_zone(heart_rate, age)
    
    # Display results
    print("\n" + "=" * 50)
    print(f"      CLINICAL REPORT: {name.upper()}")
    print("=" * 50)
    
    print(f"\n❤️ HEART RATE: {heart_rate} bpm")
    print(f"   • Classification: {classification}")
    print(f"   • Advice: {advice}")
    
    print(f"\n🏃 TRAINING ANALYSIS:")
    print(f"   • Training Zone: {training_zone}")
    print(f"   • Max HR (220-age): {220 - age} bpm")
    
    # Multiple readings (bonus)
    more_readings = input("\n📊 Add more readings? (y/n): ").lower()
    if more_readings == 'y':
        readings = [heart_rate]
        print("\nEnter additional readings (type 'done' to finish):")
        while True:
            val = input("Reading: ")
            if val.lower() == 'done':
                break
            try:
                readings.append(int(val))
            except ValueError:
                print("Invalid input. Enter a number or 'done'.")
        
        stats = analyze_multiple_readings(readings)
        print("\n📈 STATISTICAL SUMMARY:")
        print(f"   • Average: {stats['average']:.0f} bpm")
        print(f"   • Min: {stats['min']} bpm")
        print(f"   • Max: {stats['max']} bpm")
        print(f"   • Range: {stats['range']} bpm")
        print(f"   • Resting estimate: {stats['resting_estimate']} bpm")
    
    print("\n" + "=" * 50)
    print("           REPORT COMPLETE")
    print("=" * 50)


if __name__ == "__main__":
    main()
