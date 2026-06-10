# Keep asking until user gets it right

while True:
    try:
        age = int(input("Enter your age: "))
        break  # Exit if successful
    except:
        print("That's not a number! Try again.")

print(f"Age accepted: {age}")