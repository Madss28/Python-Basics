# Handle division by zero

try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(f"100 / {num} = {result}")
except ValueError:
    print("That's not a number!")
except ZeroDivisionError:
    print("Can't divide by zero!")