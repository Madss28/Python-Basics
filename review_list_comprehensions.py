"""
REVIEW: List Comprehensions
Test your knowledge without looking at notes first.
"""

print("=" * 50)
print("REVIEW: LIST COMPREHENSIONS")
print("=" * 50)

# ----- PART 1: BASIC LIST COMPREHENSIONS -----
print("\n--- BASIC ---")

# 1. Numbers 0-9
nums = [i for i in range(10)]
print(f"1. Numbers 0-9: {nums}")

# 2. Numbers 1-10
nums = [i for i in range(1, 11)]
print(f"2. Numbers 1-10: {nums}")

# 3. Squares of 0-9
squares = [i ** 2 for i in range(10)]
print(f"3. Squares 0-9: {squares}")

# 4. Multiply each number by 2
numbers = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in numbers]
print(f"4. Doubled: {doubled}")

# 5. Convert to uppercase
names = ["john", "sarah", "mike"]
upper_names = [name.upper() for name in names]
print(f"5. Uppercase names: {upper_names}")


# ----- PART 2: WITH CONDITION (FILTER) -----
print("\n--- WITH CONDITION (filter) ---")

# 6. Even numbers 0-19
evens = [i for i in range(20) if i % 2 == 0]
print(f"6. Evens 0-19: {evens}")

# 7. Numbers greater than 10
nums = [5, 12, 8, 20, 3, 15, 7]
big_nums = [n for n in nums if n > 10]
print(f"7. Numbers > 10: {big_nums}")

# 8. Names starting with 'S'
names = ["Sarah", "John", "Steve", "Emma", "Sam"]
s_names = [name for name in names if name[0] == 'S']
print(f"8. Names starting with S: {s_names}")

# 9. Words longer than 4 letters
words = ["cat", "elephant", "dog", "butterfly", "bird"]
long_words = [w for w in words if len(w) > 4]
print(f"9. Words longer than 4 letters: {long_words}")


# ----- PART 3: TRANSFORMATION + CONDITION -----
print("\n--- TRANSFORMATION + CONDITION ---")

# 10. Square only even numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8]
squared_evens = [n ** 2 for n in nums if n % 2 == 0]
print(f"10. Squares of evens: {squared_evens}")

# 11. Uppercase only names starting with 'S'
names = ["Sarah", "John", "Steve", "Emma", "Sam"]
upper_s_names = [name.upper() for name in names if name[0] == 'S']
print(f"11. Uppercase S-names: {upper_s_names}")


# ----- PART 4: WORKING WITH DICTIONARIES -----
print("\n--- WORKING WITH DICTIONARIES ---")

# 12. List of dictionaries
patients = [
    {"name": "John", "age": 45, "hr": 72},
    {"name": "Sarah", "age": 32, "hr": 68},
    {"name": "Mike", "age": 28, "hr": 75}
]

# 13. Extract all ages
ages = [p["age"] for p in patients]
print(f"13. All ages: {ages}")

# 14. Extract all names
names = [p["name"] for p in patients]
print(f"14. All names: {names}")

# 15. Names of patients over 30
older_names = [p["name"] for p in patients if p["age"] > 30]
print(f"15. Patients over 30: {older_names}")

# 16. Heart rates of patients under 30
young_hr = [p["hr"] for p in patients if p["age"] < 30]
print(f"16. Heart rates under 30: {young_hr}")


# ----- PART 5: IF-ELSE IN COMPREHENSION -----
print("\n--- IF-ELSE (choose) ---")

# 17. Label even/odd
numbers = [1, 2, 3, 4, 5]
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(f"17. Even/odd labels: {labels}")

# 18. Categorize ages
ages = [15, 25, 35, 45, 55, 65]
categories = ["Young" if age < 30 else "Middle" if age < 50 else "Senior" for age in ages]
print(f"18. Age categories: {categories}")


# ----- PART 6: PRACTICE EXERCISES -----
print("\n--- PRACTICE EXERCISES (Test Yourself) ---")

# Exercise A: Create list of numbers 1-15
ex_a = [i for i in range(1, 16)]
print(f"A. Numbers 1-15: {ex_a}")

# Exercise B: Create list of numbers multiplied by 3
nums = [2, 4, 6, 8, 10]
ex_b = [n * 3 for n in nums]
print(f"B. Multiplied by 3: {ex_b}")

# Exercise C: Get only numbers less than 5
nums = [3, 8, 1, 6, 2, 9, 4]
ex_c = [n for n in nums if n < 5]
print(f"C. Numbers less than 5: {ex_c}")

# Exercise D: Get length of each word
words = ["python", "java", "javascript", "c"]
ex_d = [len(w) for w in words]
print(f"D. Word lengths: {ex_d}")

# Exercise E: Square only odd numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ex_e = [n ** 2 for n in nums if n % 2 != 0]
print(f"E. Squares of odd numbers: {ex_e}")

print("\n✅ List Comprehensions review complete!")