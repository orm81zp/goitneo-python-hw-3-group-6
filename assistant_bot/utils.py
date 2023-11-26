import pickle
from pathlib import Path

from .address_book import Record, AddressBook

class InputBotExseption(Exception):
    pass


DUMP_FILE = None
DUMP_FILE_NAME = "assistant_bot_data.bin"


def init_address_book(dump_file_path: Path):
    global DUMP_FILE
    DUMP_FILE = dump_file_path

    if dump_file_path and dump_file_path.exists():
        with open(dump_file_path, "rb") as fh:
            address_book = pickle.load(fh)
            return address_book
    else:
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
    COMMANDS = {
        "add": "used to add a phone number: \"add [username] [phone]\"",
        "remove": "used to remove a phone number: \"remove [username] [phone]\"",
        "change": "used to change a phone number: \"change [username] [phone]\"",
        "phone": "used to display a phone number(s): \"phone [username]\"",
        "all": "used to display all contacts: \"all\"",
        "add-birthday": "used to add a birthday: \"add-birthday [username] [birthday]\"",
        "show-birthday": "used to display a birthday: \"show-birthday [username]\"",
        "birthdays": "used to display birthdays that will happen in the next week: \"birthdays\"",
        "remove-contact": "used to remove a contact: \"remove-contact [username]\"",
        "hello": "used to display a welcome message: \"hello\"",
        "close or exit": "used to close the program: \"exit\"",
        "help": "used to display available commands: \"help\"",
    }

    output = "Please, use only the following commands:\n"
    for command in COMMANDS:
        output += "{:<20} - {:<30}\n".format(command, COMMANDS[command])
    output += "\n"
    return output

def terminate(book: AddressBook):
    global DUMP_FILE
    if book.has_data() and DUMP_FILE:
        with open(DUMP_FILE, "wb") as fh:
            pickle.dump(book, fh)
    
    return "Good bye!"

def show_hello():
    return "How can I help you?"

def parse_input(user_input):
    if not user_input:
        raise InputBotExseption
    
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def is_yes_prompt(user_input):
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

def birthdays(book: AddressBook):
    birthdays = book.birthdays()
    return birthdays if birthdays else "There are no data to display."

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

