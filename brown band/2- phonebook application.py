def add_contact(phonebook, name, phone):
    phonebook[name] = phone
    print(f"Contact {name} added successfully.")


def search_contact(phonebook, name):
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print(f"Contact {name} not found.")

3
def update_contact(phonebook, name, new_phone):
    if name in phonebook:
        phonebook[name] = new_phone
        print(f"Contact {name} updated successfully.")
    else:
        print(f"Contact {name} not found.")


def delete_contact(phonebook, name):
    if name in phonebook:
        del (phonebook[name])
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")


def display_phonebook(phonebook):
    if phonebook:
        print("Phonebook Contacts:")
        for name, phone in phonebook.items():
            print(f"{name}: {phone}")
    else:
        print("Phonebook is empty.")


def main():
    phonebook = {}
    while True:
        print("\nPhonebook Application")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display All Contacts")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            add_contact(phonebook, name, phone)
        elif choice == '2':
            name = input("Enter name to search: ")
            search_contact(phonebook, name)
        elif choice == '3':
            name = input("Enter name to update: ")
            new_phone = input("Enter new phone number: ")
            update_contact(phonebook, name, new_phone)
        elif choice == '4':
            name = input("Enter name to delete: ")
            delete_contact(phonebook, name)
        elif choice == '5':
            display_phonebook(phonebook)
        elif choice == '6':
            print("Exiting phonebook application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
