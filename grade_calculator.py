# DAY 3 - ALL EXERCISES TOGETHER
# Number Checker + Grade Calculator + Even/Odd Checker

print("=" * 50)
print("     DAY 3: CONDITIONALS PRACTICE")
print("=" * 50)

# EXERCISE 1: Number Checker
print("\n📌 EXERCISE 1: NUMBER CHECKER")
print("-" * 30)
number = float(input("Enter a number: "))

if number > 0:
    print(f"  → {number} is POSITIVE")
elif number < 0:
    print(f"  → {number} is NEGATIVE")
else:
    print(f"  → {number} is ZERO")

# EXERCISE 3: Even or Odd (using the same number)
print("\n📌 EXERCISE 3: EVEN OR ODD")
print("-" * 30)
# Convert to integer for even/odd check
whole_number = int(number)
if whole_number % 2 == 0:
    print(f"  → {whole_number} is EVEN")
else:
    print(f"  → {whole_number} is ODD")

# EXERCISE 2: Grade Calculator
print("\n📌 EXERCISE 2: GRADE CALCULATOR")
print("-" * 30)
score = float(input("Enter your score (0-100): "))

if score < 0 or score > 100:
    print("  → ❌ Invalid score! Must be between 0 and 100.")
elif score >= 90:
    print(f"  → Score: {score} → Grade: A 🎉")
elif score >= 80:
    print(f"  → Score: {score} → Grade: B 👍")
elif score >= 70:
    print(f"  → Score: {score} → Grade: C 📚")
elif score >= 60:
    print(f"  → Score: {score} → Grade: D ⚠️")
else:
    print(f"  → Score: {score} → Grade: F ❌")

print("\n" + "=" * 50)
print("     PRACTICE COMPLETE! 🎉")
print("=" * 50)