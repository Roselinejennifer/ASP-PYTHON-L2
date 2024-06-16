# Initialize an empty grocery list
grocery_list = []

# Function to print all items in the grocery list
def print_grocery_list():
    if not grocery_list:
        print("Grocery list is empty.")
    else:
        print("Grocery List:")
        for index, item in enumerate(grocery_list, start=1):
            print(f"{index}. {item}")

# Append items to the grocery list
def add_item(item):
    grocery_list.append(item)
    print(f"{item} added to the grocery list.")

# Remove an item from the grocery list
def remove_item(item):
    if item in grocery_list:
        grocery_list.remove(item)
        print(f"{item} removed from the grocery list.")
    else:
        print(f"{item} is not in the grocery list.")

# Sort the items in the grocery list
def sort_items():
    grocery_list.sort()
    print("Grocery list sorted.")

# Main loop to interact with the grocery list
while True:
    print("\nGrocery List Menu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. Sort items")
    print("4. Print grocery list")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        item = input("Enter the item to add: ")
        add_item(item)
    elif choice == '2':
        item = input("Enter the item to remove: ")
        remove_item(item)
    elif choice == '3':
        sort_items()
    elif choice == '4':
        print_grocery_list()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")