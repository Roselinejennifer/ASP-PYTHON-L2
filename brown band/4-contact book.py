import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({"name": name, "phone_number": phone_number, "email": email})
    save_contacts(contacts)
    print("Contact added successfully.")

def remove_contact(contacts):
    name = input("Enter contact name to remove: ")
    contact = next((contact for contact in contacts if contact['name'] == name), None)
    if contact:
        contacts.remove(contact)
        save_contacts(contacts)
        print("Contact removed successfully.")
    else:
        print("Contact not found.")

def update_contact(contacts):
    name = input("Enter contact name to update: ")
    contact = next((contact for contact in contacts if contact['name'] == name), None)
    if contact:
        phone_number = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        contact['phone_number'] = phone_number
        contact['email'] = email
        save_contacts(contacts)
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def search_contacts(contacts):
    query = input("Enter name, phone number, or email to search: ").lower()
    results = [contact for contact in contacts if query in contact['name'].lower() or query in contact['phone_number'] or query in contact['email'].lower()]
    if results:
        print("Search results:")
        for contact in results:
            print(contact)
    else:
        print("No matching contacts found.")

def sort_contacts(contacts):
    criteria = input("Sort by 'name', 'phone_number', or 'email': ")
    if criteria in {'name', 'phone_number', 'email'}:
        sorted_contacts = sorted(contacts, key=lambda x: x[criteria].lower())
        print("Sorted contacts:")
        for contact in sorted_contacts:
            print(contact)
    else:
        print("Invalid sorting criteria.")

def filter_contacts(contacts):
    criteria = input("Filter by 'name', 'phone_number', or 'email': ")
    value = input(f"Enter the value to filter by {criteria}: ").lower()
    filtered_contacts = [contact for contact in contacts if value in contact[criteria].lower()]
    if filtered_contacts:
        print("Filtered contacts:")
        for contact in filtered_contacts:
            print(contact)
    else:
        print("No matching contacts found.")

def display_menu():
    print("\nContact Book Menu")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Update Contact")
    print("4. Search Contacts")
    print("5. Sort Contacts")
    print("6. Filter Contacts")
    print("7. Exit")

def contact_book_app():
    contacts = load_contacts()
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            remove_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            search_contacts(contacts)
        elif choice == '5':
            sort_contacts(contacts)
        elif choice == '6':
            filter_contacts(contacts)
        elif choice == '7':
            print("Exiting the contact book application.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the contact book application
if __name__ == "__main__":
    contact_book_app()
