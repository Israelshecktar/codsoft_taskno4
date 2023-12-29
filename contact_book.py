def welcome():
    """This function displays a welcome message"""
    print("Welcome to Shecktar Contact Book App")

def main():
    welcome()
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
