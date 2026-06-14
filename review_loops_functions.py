"""
REVIEW: Loops and Functions
Test your knowledge without looking at notes first.
"""

print("=" * 50)
print("REVIEW: LOOPS & FUNCTIONS")
print("=" * 50)

# ----- PART 1: FOR LOOPS -----
print("\n--- FOR LOOPS ---")

# 1. Print numbers 1-10
print("1. Numbers 1-10:")
for i in range(1, 11):
    print(f"   {i}", end=" ")
print("\n")

# 2. Print squares of numbers 1-5
print("2. Squares of 1-5:")
for i in range(1, 6):
    print(f"   {i}² = {i ** 2}")

# 3. Loop through a list
fruits = ["apple", "banana", "cherry"]
print("3. Fruits list:")
for fruit in fruits:
    print(f"   - {fruit}")

# 4. Loop with index using enumerate
print("4. Fruits with index:")
for i, fruit in enumerate(fruits):
    print(f"   {i}: {fruit}")


# ----- PART 2: WHILE LOOPS -----
print("\n--- WHILE LOOPS ---")

# 1. Countdown from 5 to 1
print("1. Countdown:")
count = 5
while count > 0:
    print(f"   {count}...")
    count -= 1
print("   Blast off!")

# 2. Keep asking until correct
print("2. Password checker (type 'python' to pass):")
password = ""
attempts = 0
while password != "python":
    password = input("   Enter password: ")
    attempts += 1
    if password != "python":
        print("   Wrong, try again")
print(f"   Correct! Took {attempts} attempt(s)")


# ----- PART 3: FUNCTIONS -----
print("\n--- FUNCTIONS ---")

# 1. Function to add two numbers
def add(a, b):
    return a + b

result = add(5, 3)
print(f"1. add(5, 3) = {result}")

# 2. Function to calculate square
def square(x):
    return x ** 2

print(f"2. square(4) = {square(4)}")
print(f"   square(10) = {square(10)}")

# 3. Function to check if number is even
def is_even(n):
    return n % 2 == 0

print(f"3. is_even(4) = {is_even(4)}")
print(f"   is_even(7) = {is_even(7)}")

# 4. Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)

bmi = calculate_bmi(70, 1.75)
print(f"4. BMI (70kg, 1.75m) = {bmi:.1f}")

# 5. Function with default parameter
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(f"5. greet('John') = {greet('John')}")
print(f"   greet('Sarah', 'Hi') = {greet('Sarah', 'Hi')}")

print("\n✅ Loops and Functions review complete!")