"""
REVIEW: Lists and Dictionaries
Test your knowledge without looking at notes first.
"""

print("=" * 50)
print("REVIEW: LISTS & DICTIONARIES")
print("=" * 50)

# ----- PART 1: LISTS -----
print("\n--- LISTS ---")

# 1. Create a list of 5 fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("1. Fruits:", fruits)

# 2. Add "fig" to the end
fruits.append("fig")
print("2. After append:", fruits)

# 3. Remove "cherry"
fruits.remove("cherry")
print("3. After remove:", fruits)

# 4. Get the first and last items
first = fruits[0]
last = fruits[-1]
print(f"4. First: {first}, Last: {last}")

# 5. Loop through and print each fruit
print("5. All fruits:")
for fruit in fruits:
    print(f"   - {fruit}")

# 6. Create a list of numbers 1-10 using range
numbers = list(range(1, 11))
print(f"6. Numbers 1-10: {numbers}")

# 7. Create a list of even numbers from numbers list
evens = [n for n in numbers if n % 2 == 0]
print(f"7. Even numbers: {evens}")


# ----- PART 2: DICTIONARIES -----
print("\n--- DICTIONARIES ---")

# 1. Create a dictionary for a patient
patient = {
    "name": "John Smith",
    "age": 45,
    "heart_rate": 72,
    "diagnosis": "Hypertension"
}
print("1. Patient:", patient)

# 2. Access and print the patient's name
print(f"2. Patient name: {patient['name']}")

# 3. Update the heart rate to 75
patient["heart_rate"] = 75
print(f"3. Updated heart rate: {patient['heart_rate']}")

# 4. Add a new key: temperature = 98.6
patient["temperature"] = 98.6
print("4. Added temperature:", patient)

# 5. Loop through and print all key-value pairs
print("5. All patient data:")
for key, value in patient.items():
    print(f"   {key}: {value}")

# 6. Create a list of patients (list of dictionaries)
patients = [
    {"name": "John", "age": 45, "hr": 72},
    {"name": "Sarah", "age": 32, "hr": 68},
    {"name": "Mike", "age": 28, "hr": 75}
]
print("6. Patients list:", patients)

# 7. Extract all names using list comprehension
names = [p["name"] for p in patients]
print(f"7. All patient names: {names}")

# 8. Extract names of patients over 30
older = [p["name"] for p in patients if p["age"] > 30]
print(f"8. Patients over 30: {older}")

print("\n✅ Lists and Dictionaries review complete!")