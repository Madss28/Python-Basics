# Heart Rate Analysis
print("=== HEART RATE ANALYSIS ===")

hr1 = int(input("Reading 1 (bpm): "))
hr2 = int(input("Reading 2 (bpm): "))
hr3 = int(input("Reading 3 (bpm): "))

average = (hr1 + hr2 + hr3) / 3
print(f"\nAverage heart rate: {average:.0f} bpm")

if average < 60:
    print("Note: Below normal range")
elif average <= 100:
    print("Note: Normal range")
else:
    print("Note: Above normal range")