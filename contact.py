def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")

    file = open("contacts.txt", "a")
    file.write(name + "," + phone + "\n")
    file.close()

    print("Contact Added Successfully!")


def view_contacts():
    file = open("contacts.txt", "r")
    contacts = file.readlines()

    if len(contacts) == 0:
        print("No contacts found")
    else:
        print("\nSaved Contacts:")
        for contact in contacts:
            name, phone = contact.strip().split(",")
            print("Name:", name, "| Phone:", phone)

    file.close()


def search_contact():
    search_name = input("Enter name to search: ")

    file = open("contacts.txt", "r")
    contacts = file.readlines()

    found = False

    for contact in contacts:
        name, phone = contact.strip().split(",")
        if search_name.lower() == name.lower():
            print("Contact Found")
            print("Name:", name)
            print("Phone:", phone)
            found = True

    if not found:
        print("Contact not found")

    file.close()


while True:
    print("\nContact Book Application")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
