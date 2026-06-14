"""
REVIEW: Error Handling (try/except)
Test your knowledge without looking at notes first.
"""

print("=" * 50)
print("REVIEW: ERROR HANDLING")
print("=" * 50)

# ----- PART 1: BASIC TRY/EXCEPT -----
print("\n--- BASIC TRY/EXCEPT ---")

# 1. Handle ValueError (bad number input)
print("1. Handling bad number input:")
try:
    num = int(input("   Enter a number: "))
    print(f"   You entered: {num}")
except ValueError:
    print("   ❌ That's not a number!")

# 2. Handle ZeroDivisionError
print("\n2. Handling division by zero:")
try:
    result = 10 / 0
    print(f"   Result: {result}")
except ZeroDivisionError:
    print("   ❌ Cannot divide by zero!")

# 3. Handle FileNotFoundError
print("\n3. Handling missing file:")
try:
    with open("missing_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("   ❌ File not found!")


# ----- PART 2: KEEP ASKING UNTIL VALID (MOST USEFUL) -----
print("\n--- KEEP ASKING UNTIL VALID ---")

# 4. Keep asking for age until valid
print("4. Getting valid age:")
while True:
    try:
        age = int(input("   Enter your age: "))
        if 0 <= age <= 120:
            print(f"   ✅ Age accepted: {age}")
            break
        else:
            print("   ❌ Age must be 0-120")
    except ValueError:
        print("   ❌ Please enter a number!")

# 5. Keep asking for a number until valid
print("\n5. Getting a valid number:")
while True:
    try:
        num = float(input("   Enter a number: "))
        print(f"   ✅ Number accepted: {num}")
        break
    except ValueError:
        print("   ❌ Please enter a valid number!")


# ----- PART 3: HANDLE MULTIPLE ERRORS -----
print("\n--- HANDLE MULTIPLE ERRORS ---")

# 6. Handle different errors differently
print("6. Calculator with multiple error handling:")
try:
    num1 = float(input("   First number: "))
    num2 = float(input("   Second number: "))
    result = num1 / num2
    print(f"   ✅ {num1} / {num2} = {result}")
except ValueError:
    print("   ❌ Please enter numbers only!")
except ZeroDivisionError:
    print("   ❌ Cannot divide by zero!")


# ----- PART 4: REAL-WORLD EXAMPLE -----
print("\n--- REAL-WORLD EXAMPLE ---")

# 7. Safe patient data input
print("7. Patient data entry (with validation):")

patients = []

while True:
    print("\n   --- New Patient ---")
    
    # Get name (no validation needed)
    name = input("   Name: ")
    
    # Get age with validation
    while True:
        try:
            age = int(input("   Age: "))
            if 0 <= age <= 120:
                break
            print("   Age must be 0-120")
        except ValueError:
            print("   Please enter a number")
    
    # Get heart rate with validation
    while True:
        try:
            hr = int(input("   Heart rate (bpm): "))
            if 30 <= hr <= 250:
                break
            print("   Heart rate must be 30-250")
        except ValueError:
            print("   Please enter a number")
    
    # Save patient
    patients.append({"name": name, "age": age, "heart_rate": hr})
    print(f"   ✅ {name} added!")
    
    # Ask to continue
    another = input("\n   Add another? (y/n): ")
    if another.lower() != 'y':
        break

# Display all patients
print("\n--- ALL PATIENTS ---")
for p in patients:
    print(f"   {p['name']}: Age {p['age']}, HR {p['heart_rate']} bpm")

print("\n✅ Error Handling review complete!")