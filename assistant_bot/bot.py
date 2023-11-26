from pathlib import Path

from .utils import (
  init_address_book, 
  parse_input, 
  show_help, 
  show_hello, 
  add_birthday, 
  show_birthday, 
  birthdays, 
  add_phone, 
  remove_phone, 
  change_phone, 
  show_phone,
  show_all,
  terminate,
  is_yes_prompt,
  remove_contact,
  DUMP_FILE_NAME,
  InputBotExseption,
)

default_dump_file_path = Path(__file__).resolve().parent.parent / DUMP_FILE_NAME

def run_bot(dump_file_path: Path = default_dump_file_path):
    book = init_address_book(dump_file_path)
    print("Welcome to the assistant bot!")
    print(show_help())

    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit", "bye", "good bye"]:
                print(terminate(book))
                break
            elif command == "hello":
                print(show_hello())
            elif command == "add-birthday":
                print(add_birthday(args, book))
            elif command == "show-birthday":
                print(show_birthday(args, book))
            elif command == "birthdays":
                print(birthdays(book))
            elif command == "add":
                print(add_phone(args, book))
            elif command == "remove":
                print(remove_phone(args, book))
            elif command == "change":
                print(change_phone(args, book))    
            elif command == "phone":
                print(show_phone(args, book))    
            elif command == "all":
                print(show_all(book))
            elif command == "remove-contact":
                user_input = input("Are you sure you want to delete the contact (y or n)? ")
                if is_yes_prompt(user_input):
                    print(remove_contact(args, book))
            elif command == "help":
                print(show_help())
            else:
                print("Invalid command. Type \"help\".")
        except InputBotExseption:
            print("Please, enter a command to begin.")
        except Exception as err:
            print("Oops! Something went wrong.", err)


if __name__ == "__main__":
    run_bot()
