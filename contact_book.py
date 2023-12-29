import random

def welcome():
    """This function displays a welcome message"""
    print("Welcome to Shecktar Contact Book App")

def add_contact(name, phone, email, address):
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}

def view_contacts():
    for name, info in contacts.items():
        print(f"\nContact: {name}")
        print(f"Phone: {info['Phone']}")
        print(f"Email: {info['Email']}")
        print(f"Address: {info['Address']}")

def search_contact(name):
    if name in contacts:
        print(f"\nContact: {name}")
        print(f"Phone: {contacts[name]['Phone']}")
        print(f"Email: {contacts[name]['Email']}")
        print(f"Address: {contacts[name]['Address']}")
    else:
        print("\nContact not found.")

def update_contact(name, phone, email, address):
    if name in contacts:
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        print(f"\nUpdated details for: {name}")
    else:
        print("\nContact not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"\nDeleted contact: {name}")
    else:
        print("\nContact not found.")

def main():
    welcome()
    contacts = {}
    while True:
        print("\nSelect operation:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        operation = input("Enter choice (1/2/3/4/5/6): ")

        if operation == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter home address: ")
            add_contact(name, phone, email, address)

        elif operation == '2':
            view_contacts()

        elif operation == '3':
            name = input("Enter name: ")
            search_contact(name)

        elif operation == '4':
            name = input("Enter name: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            address = input("Enter new home address: ")
            update_contact(name, phone, email, address)

        elif operation == '5':
            name = input("Enter name: ")
            delete_contact(name)

        elif operation == '6':
            break

        else:
            print("\nInvalid input")

# Call the main function
if __name__ == "__main__":
    main()
