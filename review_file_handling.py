"""
REVIEW: File I/O
Test your knowledge without looking at notes first.
"""

import os

print("=" * 50)
print("REVIEW: FILE I/O")
print("=" * 50)

# ----- PART 1: WRITE TO FILE -----
print("\n--- WRITING TO FILES ---")

# 1. Write to a file (overwrites existing)
print("1. Writing to test.txt...")
with open("test.txt", "w") as file:
    file.write("First line\n")
    file.write("Second line\n")
    file.write("Third line\n")
print("   ✅ Written successfully!")

# 2. Append to a file (adds to end)
print("\n2. Appending to test.txt...")
with open("test.txt", "a") as file:
    file.write("Fourth line (appended)\n")
    file.write("Fifth line (appended)\n")
print("   ✅ Appended successfully!")


# ----- PART 2: READ FROM FILE -----
print("\n--- READING FROM FILES ---")

# 3. Read entire file at once
print("3. Reading entire file:")
with open("test.txt", "r") as file:
    content = file.read()
    print(content)

# 4. Read line by line (BEST WAY)
print("4. Reading line by line:")
with open("test.txt", "r") as file:
    for line in file:
        print(f"   {line.strip()}")

# 5. Read all lines into a list
print("5. Reading into a list:")
with open("test.txt", "r") as file:
    lines = file.readlines()
    print(f"   First line: {lines[0].strip()}")
    print(f"   Total lines: {len(lines)}")


# ----- PART 3: CHECK IF FILE EXISTS -----
print("\n--- CHECKING FILES ---")

# 6. Check if file exists before reading
filename = "test.txt"
if os.path.exists(filename):
    print(f"6. {filename} exists!")
    with open(filename, "r") as file:
        first_line = file.readline()
        print(f"   First line: {first_line.strip()}")
else:
    print(f"6. {filename} does not exist!")

# 7. Check if a non-existent file exists
missing_file = "does_not_exist.txt"
if os.path.exists(missing_file):
    print(f"7. {missing_file} exists!")
else:
    print(f"7. {missing_file} does NOT exist!")


# ----- PART 4: PRACTICE EXERCISES -----
print("\n--- PRACTICE EXERCISES ---")

# 8. Write user input to file
print("8. Saving user input to file...")
name = input("   Enter your name: ")
with open("user.txt", "w") as file:
    file.write(f"Name: {name}\n")
print("   ✅ Saved!")

# 9. Read it back
print("9. Reading saved data:")
with open("user.txt", "r") as file:
    for line in file:
        print(f"   {line.strip()}")

print("\n✅ File I/O review complete!")