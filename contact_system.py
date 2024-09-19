import json
import os

# Function to load contacts from file
def load_contacts(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    else:
        return {}

# Function to save contacts to file
def save_contacts(file_name, contacts):
    with open(file_name, 'w') as file:
        json.dump(contacts, file, indent=4)

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    if name in contacts:
        print(f"A contact with the name {name} already exists.")
    else:
        contacts[name] = {"phone": phone, "email": email}
        print(f"Contact {name} added successfully.")

# Function to view all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

# Function to edit an existing contact
def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ").strip()
    if name in contacts:
        phone = input(f"Enter new phone number for {name} (or press Enter to keep current): ").strip()
        email = input(f"Enter new email address for {name} (or press Enter to keep current): ").strip()

        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email

        print(f"Contact {name} updated successfully.")
    else:
        print(f"No contact found with the name {name}.")

# Function to delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"No contact found with the name {name}.")

# Main program
def main():
    file_name = "contacts.json"
    contacts = load_contacts(file_name)

    while True:
        print("\nContact Manager")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(file_name, contacts)
            print("Contacts saved. Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

# Run the program
if __name__ == "__main__":
    main()
