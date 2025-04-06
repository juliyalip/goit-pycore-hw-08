from functions import parse_input,add_contact, change_contact, show_phone, add_birthday, show_birthday, delete_contact
from classes import AddressBook
from api_functions import save_data, load_data

def main():
    book = load_data()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        print("command from input:", command, *args)
        
        if command in ["close", "exit"]:
            print("Good bye!")
            save_data(book)
            break

        elif command == "hello":
            print("How can I help you?")
            
        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "add-birthday":
            print(add_birthday(args, book))
        
        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(book.get_upcoming_birthdays())

        elif command == "delete":
            print(delete_contact(args, book))

        elif command =="all":
            print(book)

      
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()