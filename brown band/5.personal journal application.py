import os
import glob
import datetime
from fpdf import FPDF

# Directory to store journal entries
JOURNAL_DIR = 'journal_entries'

# Ensure the journal directory exists
if not os.path.exists(JOURNAL_DIR):
    os.makedirs(JOURNAL_DIR)


def add_entry():
    title = input("Enter entry title: ")
    content = input("Enter entry content: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    filename = f"{JOURNAL_DIR}/{title.replace(' ', '_')}.txt"
    with open(filename, 'w') as file:
        file.write(f"Title: {title}\n")
        file.write(f"Timestamp: {timestamp}\n")
        file.write(f"Content:\n{content}\n")

    print("Entry added successfully.")


def read_entry():
    title = input("Enter entry title to read: ")
    filename = f"{JOURNAL_DIR}/{title.replace(' ', '_')}.txt"
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    else:
        print("Entry not found.")


def update_entry():
    title = input("Enter entry title to update: ")
    filename = f"{JOURNAL_DIR}/{title.replace(' ', '_')}.txt"
    if os.path.exists(filename):
        content = input("Enter new content: ")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, 'w') as file:
            file.write(f"Title: {title}\n")
            file.write(f"Timestamp: {timestamp}\n")
            file.write(f"Content:\n{content}\n")

        print("Entry updated successfully.")
    else:
        print("Entry not found.")


def delete_entry():
    title = input("Enter entry title to delete: ")
    filename = f"{JOURNAL_DIR}/{title.replace(' ', '_')}.txt"
    if os.path.exists(filename):
        os.remove(filename)
        print("Entry deleted successfully.")
    else:
        print("Entry not found.")


def search_entries():
    keyword = input("Enter keyword to search: ")
    files = glob.glob(f"{JOURNAL_DIR}/*.txt")
    found = False
    for file in files:
        with open(file, 'r') as f:
            content = f.read()
            if keyword.lower() in content.lower():
                print(f"\nFound in {file}:\n")
                print(content)
                found = True
    if not found:
        print("No entries found with the given keyword.")


def export_to_pdf():
    title = input("Enter entry title to export to PDF: ")
    filename = f"{JOURNAL_DIR}/{title.replace(' ', '_')}.txt"
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()

        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)
        for line in content.split('\n'):
            pdf.cell(200, 10, txt=line, ln=True)

        pdf_output = f"{JOURNAL_DIR}/{title.replace(' ', '_')}.pdf"
        pdf.output(pdf_output)
        print(f"Entry exported to {pdf_output} successfully.")
    else:
        print("Entry not found.")


def display_menu():
    print("\nJournal App Menu")
    print("1. Add Entry")
    print("2. Read Entry")
    print("3. Update Entry")
    print("4. Delete Entry")
    print("5. Search Entries")
    print("6. Export Entry to PDF")
    print("7. Exit")


def journal_app():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_entry()
        elif choice == '2':
            read_entry()
        elif choice == '3':
            update_entry()
        elif choice == '4':
            delete_entry()
        elif choice == '5':
            search_entries()
        elif choice == '6':
            export_to_pdf()
        elif choice == '7':
            print("Exiting the journal app.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    journal_app()
