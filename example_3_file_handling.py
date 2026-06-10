# Handle missing files

filename = input("Enter filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print(f"File contains: {content}")
except FileNotFoundError:
    print(f"File '{filename}' not found!")
except:
    print("Something else went wrong")