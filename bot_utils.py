
from address_book import Record, AddressBook

class InputBotExseption(Exception):
    pass

COMMANDS_INFO = {
    "add": "used to add a phone number: \"add [username] [phone]\"",
    "remove": "used to remove a phone number: \"remove [username] [phone]\"",
    "change": "used to change a contact phone number: \"change [username] [phone]\"",
    "phone": "used to display a phone number: \"phone [username]\"",
    "all": "used to display all saved contacts: \"all\"",
    "add-birthday": "used to add a birthday: \"add-birthday [username] [birthday]\"",
    "show-birthday": "used to display a birthday: \"show-birthday [username]\"",
    "birthdays": "used to display birthdays that will happen in the next week: \"birthdays\"",
    "delete-contact": "used to delete a contact: \"delete-contact [username]\"",
    "hello": "used to display a welcome message: \"hello\"",
    "close or exit": "used to terminate the program: \"exit\"",
    "help": "used to display commands the Bot commands: \"help\"",
}

def init_address_book():
    address_book = AddressBook()
    return address_book

def input_error(error):
    """Decorator takes an error message and return the error"""
    def error_handler(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError:
                return error
            except IndexError:
                return error
        return inner
    return error_handler

def show_help():
    output = "Please, use only the following commands:\n"
    for command in COMMANDS_INFO:
        output += "{:<20} - {:<30}\n".format(command, COMMANDS_INFO[command])
    output += "\n"
    return output

def show_hello():
    return "How can I help you?"

def parse_input(user_input):
    if not user_input:
        raise InputBotExseption
    
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def is_yes_prompt(user_input):
    """Checks if the value entered as yes or y"""
    if not user_input:
        raise InputBotExseption

    prompt = user_input.strip().lower()
    return prompt in ["yes", "y"]

@input_error("Give me name, old phone, new phone please.")
def change_phone(args, book: AddressBook):
    name, old_phone, new_phone = args
    contact = book.find(name)

    if contact is not None:
        return contact.edit_phone(old_phone, new_phone)
    else:
        return "Contact not found."

@input_error("Give me name please.")
def show_phone(args, book: AddressBook):
    name = args[0]
    contact = book.find(name)

    if contact:
        return contact.find_phones()
    else:
        return "Contact not found."

def show_all(book: AddressBook):
    all_contacts = book.find_all()
    return all_contacts if all_contacts else "There are no contacts to display."

    
@input_error("Give me name and birthday.")
def add_birthday(args, book: AddressBook):
    name, birthday = args

    contact = book.find(name)
    if contact:
        return contact.add_birthday(birthday)
    else:
        contact = Record(name)
        result_add_birthday = contact.add_birthday(birthday)

        if contact.birthday is not None:
            book.add_record(contact)
        
        return result_add_birthday

@input_error("Give me name please.")
def show_birthday(args, book: AddressBook):
    name = args[0]

    contact = book.find(name)
    if contact:
        return contact.find_birthday()
    else:
        return "Contact not found."

def show_birthdays(book: AddressBook):
    birthdays = book.get_birthdays_per_week()
    return birthdays if birthdays else "There are no birthdays to display."

@input_error("Give me name and phone please.")
def add_phone(args, book: AddressBook):
    name, phone = args
    contact = book.find(name)

    if contact:
        return contact.add_phone(phone)
    else:
        contact = Record(name)
        result_add_phone = contact.add_phone(phone)
        book.add_record(contact)
        return result_add_phone

@input_error("Give me name and phone please.")
def remove_phone(args, book: AddressBook):
    name, phone = args
    contact = book.find(name)

    if contact:
        return contact.remove_phone(phone)
    else:
        return "Contact not found."

@input_error("Give me name please.")
def remove_contact(args, book: AddressBook):
    name = args[0]
    contact = book.find(name)

    if contact:
        return book.delete(name)
    else:
        return "Contact not found."


# COMMANDS = {
#     "hello": show_hello,
#     "add": add_phone,
#     "change": change_phone,
#     "phone": show_phone,
#     "all": show_all,
#     "help": show_help,
#     "close or exit": "used to terminate the program",
# }

# def command_handler(command, args, address_book):
#     pass