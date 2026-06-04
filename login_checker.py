# LOGIN CHECKER
# Demonstrates: conditionals, logical operators, loops

print("=" * 40)
print("         LOGIN SYSTEM")
print("=" * 40)

# Pre-set credentials (in real life, this would be in a database)
CORRECT_USERNAME = "biomed_student"
CORRECT_PASSWORD = "datascience2026"

# Track attempts
max_attempts = 3
attempts = 0
logged_in = False

print(f"\nYou have {max_attempts} attempts.\n")

# Loop until successful login or too many attempts
while attempts < max_attempts and not logged_in:
    attempts += 1
    
    print(f"Attempt {attempts} of {max_attempts}")
    print("-" * 25)
    
    # Get user input
    username = input("Username: ")
    password = input("Password: ")
    
    # Check credentials
    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        print("\n✅ LOGIN SUCCESSFUL!")
        print(f"Welcome back, {username}!")
        logged_in = True
        
    elif username != CORRECT_USERNAME and password == CORRECT_PASSWORD:
        print("\n❌ LOGIN FAILED")
        print(f"Username '{username}' not found.")
        remaining = max_attempts - attempts
        print(f"Attempts remaining: {remaining}")
        
    elif username == CORRECT_USERNAME and password != CORRECT_PASSWORD:
        print("\n❌ LOGIN FAILED")
        print("Incorrect password.")
        remaining = max_attempts - attempts
        print(f"Attempts remaining: {remaining}")
        
    else:
        print("\n❌ LOGIN FAILED")
        print("Both username AND password are incorrect.")
        remaining = max_attempts - attempts
        print(f"Attempts remaining: {remaining}")

# After loop ends - check if logged in
if not logged_in:
    print("\n" + "=" * 40)
    print("🔒 ACCOUNT LOCKED")
    print("Too many failed attempts.")
    print("Please contact support.")
    print("=" * 40)
else:
    print("\n" + "=" * 40)
    print("    WELCOME TO THE SYSTEM")
    print("=" * 40)
