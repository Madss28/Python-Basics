# EVEN OR ODD CHECKER
# Exercise 3 - Day 3

print("=== EVEN OR ODD CHECKER ===")

# Get number from user
number = int(input("Enter a whole number: "))

# Check if even or odd using modulo operator (%)
# Even numbers divide by 2 with NO remainder
if number % 2 == 0:
    print(f"{number} is EVEN ✅")
else:
    print(f"{number} is ODD 🔢")

# Bonus: Extra info about the number
if number == 0:
    print("Zero is a special even number!")
elif number % 2 == 0:
    print(f"{number} is divisible by 2.")
else:
    print(f"{number} leaves a remainder of 1 when divided by 2.")