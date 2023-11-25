import bot_utils
from bot_utils import InputBotExseption

def main():
    address_book = bot_utils.init_address_book()
    print("Welcome to the assistant bot!")
    print(bot_utils.show_help())

    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = bot_utils.parse_input(user_input)

            if command in ["close", "exit", "bye", "good bye"]:
                print("Good bye!")
                break
            elif command == "hello":
                print(bot_utils.show_hello())
            elif command == "add-birthday":
                print(bot_utils.add_birthday(args, address_book))
            elif command == "show-birthday":
                print(bot_utils.show_birthday(args, address_book))
            elif command == "birthdays":
                print(bot_utils.show_birthdays(address_book))
            elif command == "add":
                print(bot_utils.add_phone(args, address_book))
            elif command == "remove":
                print(bot_utils.remove_phone(args, address_book))
            elif command == "change":
                print(bot_utils.change_phone(args, address_book))    
            elif command == "phone":
                print(bot_utils.show_phone(args, address_book))    
            elif command == "all":
                print(bot_utils.show_all(address_book))
            elif command == "delete-contact":
                user_input = input("Are you sure you want to delete the contact? (y or n): ")
                if bot_utils.is_yes_prompt(user_input):
                    print(bot_utils.remove_contact(args, address_book))
            elif command == "help":
                print(bot_utils.show_help())
            else:
                print("Invalid command. Type \"help\" to see a list of commands.")
        except InputBotExseption:
            print("Please, enter a command to begin.")
        except Exception as err:
            print("Oops! Something went wrong.", err)


if __name__ == "__main__":
    main()
