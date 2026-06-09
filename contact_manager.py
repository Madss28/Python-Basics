"""
CONTACT MANAGER
Save and manage contacts permanently.
Demonstrates: file read/write, search, delete by line
"""

import os

CONTACTS_FILE = "contacts.txt"

def load_contacts():
    """Load contacts from file into list"""
    contacts = []
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    name, phone, email = parts
                    contacts.append({"name": name, "phone": phone, "email": email})
    return contacts

def save_contacts(contacts):
    """Save contacts list to file"""
    with open(CONTACTS_FILE, "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone']},{contact['email']}\n")

def add_contact(contacts):
    """Add a new contact"""
    print("\n--- NEW CONTACT ---")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"\n✅ {name} added to contacts!")

def view_contacts(contacts):
    """View all contacts"""
    if not contacts:
        print("\n📭 No contacts saved yet.")
        return
    
    print("\n" + "="*50)
    print("        YOUR CONTACTS")
    print("="*50)
    
    for i, contact in enumerate(contacts, 1):
        print(f"\n{i}. {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")
    
    print(f"\n📊 Total: {len(contacts)} contacts")

def search_contact(contacts):
    """Search for a contact by name"""
    if not contacts:
        print("\n📭 No contacts to search.")
        return
    
    search = input("\nEnter name to search: ").lower()
    found = []
    
    for contact in contacts:
        if search in contact['name'].lower():
            found.append(contact)
    
    if found:
        print(f"\n✅ Found {len(found)} contact(s):")
        for contact in found:
            print(f"   • {contact['name']} - {contact['phone']}")
    else:
        print(f"\n❌ No contact found with '{search}'")

def delete_contact(contacts):
    """Delete a contact by name"""
    if not contacts:
        print("\n📭 No contacts to delete.")
        return
    
    view_contacts(contacts)
    name = input("\nEnter exact name to delete: ")
    
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == name.lower():
            contacts.pop(i)
            save_contacts(contacts)
            print(f"\n✅ {name} deleted!")
            return
    
    print(f"\n❌ '{name}' not found.")

def main():
    contacts = load_contacts()
    
    print("\n📞 WELCOME TO CONTACT MANAGER")
    
    while True:
        print("\n1. Add contact")
        print("2. View all contacts")
        print("3. Search contact")
        print("4. Delete contact")
        print("5. Exit")
        
        choice = input("\nChoice: ")
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("\n👋 Goodbye! Your contacts are saved.")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()