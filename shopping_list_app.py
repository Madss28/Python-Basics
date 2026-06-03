# SHOPPING LIST APP
# Demonstrates: lists, indexing, methods, user input, loops, conditionals

print("=" * 40)
print("     WELCOME TO SHOPPING LIST APP")
print("=" * 40)

# Start with empty list
shopping_list = []

while True:
    # Display menu
    print("\n" + "-" * 30)
    print("What would you like to do?")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Find item position")
    print("5. Clear entire list")
    print("6. Exit")
    print("-" * 30)
    
    choice = input("Enter choice (1-6): ")
    
    # ADD ITEM
    if choice == "1":
        item = input("What item would you like to add? ")
        shopping_list.append(item)
        print(f"✓ '{item}' added!")
        print(f"Current list: {shopping_list}")
    
    # REMOVE ITEM
    elif choice == "2":
        if len(shopping_list) == 0:
            print("⚠️ List is empty! Nothing to remove.")
        else:
            item = input("Which item would you like to remove? ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"✓ '{item}' removed!")
                print(f"Current list: {shopping_list}")
            else:
                print(f"✗ '{item}' not found in your list.")
    
    # VIEW LIST
    elif choice == "3":
        if len(shopping_list) == 0:
            print("📋 Your shopping list is empty.")
        else:
            print("\n📋 YOUR SHOPPING LIST:")
            print("-" * 25)
            # enumerate gives both position (starting at 1) and item
            for position, item in enumerate(shopping_list, start=1):
                print(f"  {position}. {item}")
            print("-" * 25)
            print(f"Total items: {len(shopping_list)}")
    
    # FIND ITEM POSITION
    elif choice == "4":
        if len(shopping_list) == 0:
            print("⚠️ List is empty! Nothing to find.")
        else:
            item = input("Which item would you like to find? ")
            if item in shopping_list:
                # index() returns Python position (starting at 0)
                position = shopping_list.index(item) + 1  # +1 for human position
                print(f"🔍 '{item}' is at position {position}")
            else:
                print(f"✗ '{item}' not found in your list.")
    
    # CLEAR ENTIRE LIST
    elif choice == "5":
        confirm = input("Are you sure? This will delete EVERYTHING (y/n): ")
        if confirm.lower() == "y":
            shopping_list.clear()
            print("🗑️ List cleared!")
        else:
            print("Clear cancelled.")
    
    # EXIT
    elif choice == "6":
        print("\n👋 Goodbye! Here's your final list:")
        if shopping_list:
            for i, item in enumerate(shopping_list, 1):
                print(f"  {i}. {item}")
        else:
            print("  (empty)")
        print("Thanks for using Shopping List App!")
        break
    
    # INVALID CHOICE
    else:
        print("✗ Invalid choice. Please enter 1-6.")

# This runs after the loop ends
print("\nProgram ended.")
