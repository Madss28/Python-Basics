# Complete calculator with error handling

print("=== SAFE CALCULATOR ===")

while True:
    print("\n1. Divide two numbers")
    print("2. Exit")
    
    choice = input("Choice: ")
    
    if choice == "2":
        print("Goodbye!")
        break
    
    if choice == "1":
        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
            result = num1 / num2
            print(f"✅ {num1} ÷ {num2} = {result}")
        except ValueError:
            print("❌ Please enter numbers only!")
        except ZeroDivisionError:
            print("❌ Cannot divide by zero!")
        except:
            print("❌ Something went wrong!")
    else:
        print("Invalid choice")