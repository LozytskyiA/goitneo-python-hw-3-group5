from address_book import AddressBook


def parse_input(user_input):
    if not user_input.strip():
        return None,
    command, *args = user_input.split()
    command = command.lower().strip()
    return command, args


def show_help():
    print("\nInstructions:")
    print('1. To add a contact, type: add "name" "phone number"')
    print('2. To change a contact\'s phone number, type: change "name" "new phone number"')
    print('3. To show a contact\'s phone number, type: phone "name"')
    print('4. To show all contacts, type: all')
    print('5. To add a birthday, type: add-birthday "name" "birthday (DD.MM.YYYY)"')
    print('6. To show a contact\'s birthday, type: show-birthday "name"')
    print('7. To show upcoming birthdays, type: birthdays')
    print('8. To get a greeting from the bot, type: hello')
    print('9. To close or exit the program, type: close or exit')


def main():
    book = AddressBook()
    print("Welcome to the address book assistant!")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, args = parse_input(user_input)
            if command == "add":
                name, phone = args
                book.add_contact(name, phone)
                print(f"Contact {name} added.")
            elif command == "change":
                name, phone = args
                book.change_contact(name, phone)
                print(f"Contact {name}'s phone number updated.")
            elif command == "phone":
                name = args[0]
                phone = book.show_phone(name)
                print(f"Phone number for {name}: {phone}")
            elif command == "all":
                all_contacts = book.show_all()
                if all_contacts:
                    print("All contacts:")
                    for contact in all_contacts:
                        print(contact)
                else:
                    print("No contacts found.")
            elif command == "add-birthday":
                name, birthday = args
                book.add_birthday(name, birthday)
                print(f"Birthday added for {name}.")
            elif command == "show-birthday":
                name = args[0]
                birthday = book.show_birthday(name)
                print(f"Birthday for {name}: {birthday}")
            elif command == "birthdays":
                upcoming_birthdays = book.get_birthdays_per_week()
                if upcoming_birthdays is not None:
                    print("Upcoming birthdays:")
                    for name_birthday in upcoming_birthdays:
                        parts = name_birthday.split(":")
                        if len(parts) == 2:
                            name, birthday = parts
                            print(f"{name.strip()}: {birthday.strip()}")
                        else:
                            print("Error: Invalid data format in upcoming birthdays")

            elif command == "hello":
                print("Hello! How can I assist you?")
            elif command == "close" or command == "exit":
                print("Goodbye!")
                break
            else:
                print("Invalid command. Type 'help' for instructions.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
