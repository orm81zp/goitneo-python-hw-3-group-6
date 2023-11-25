from collections import UserDict
from datetime import datetime
import re

from get_birthdays_per_week import get_birthdays_per_week

TEXT = {
    "PHONE_VALIDATION": "Phone number failed validation, must consist of 10 digits",
    "PHONE_NUMBER_NOT_FOUND": "Phone number not found.",
    "PHONE_NUMBER_UPDATED": "Phone number updated.",
    "PHONE_NUMBER_ADDED": "Phone number added.",
    "PHONE_NUMBER_DELETED": "Phone number deleted.",
    "PHONE_NUMBER_EXISTS": "Phone number already exists. Use \"change [username] [phone]\" if you want to update it.",
    "BIRTHDAY_ADDED": "Birthday added.",
    "BIRTHDAY_VALIDATION": "Birthday failed validation, should be \"DD.MM.YYYY\" format.",
    "BIRTHDAY_NOT_FOUND": "Birthday not found. Use \"add-birthday [username] [birthday]\" to add one.",
    "CONTACT_DELETED": "Contact deleted",
    "CONTACT_NOT_FOUND": "Contact not found",
    "NO_DATA": "There are no data to display."
}

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    pass


class Birthday(Field):
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def is_valid_phone_number(self, phone_number):
        is_counts = len(phone_number) == 10
        is_all_numbers = all(True for number in phone_number if number.isdecimal())

        return True if is_counts and is_all_numbers else False

    def is_valid_birthday(self, birthday):
        is_birthday_matched = re.match(r"^\d{2}\.\d{2}\.\d{4}$", birthday)
        return True if is_birthday_matched else False
    
    def is_phone_number_exists(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return True
        return False

    def add_phone(self, phone_number):
        if self.is_valid_phone_number(phone_number):
            if not self.is_phone_number_exists(phone_number):
                self.phones.append(Phone(phone_number))
                return TEXT["PHONE_NUMBER_ADDED"]
            else:
                return TEXT["PHONE_NUMBER_EXISTS"]
        else:
            return TEXT["PHONE_VALIDATION"]

    def add_birthday(self, birthday: str):
        birthday = birthday.strip()
        if self.is_valid_birthday(birthday):
            self.birthday = Birthday(birthday)
            return TEXT["BIRTHDAY_ADDED"]
        else:
            return TEXT["BIRTHDAY_VALIDATION"]

    def find_birthday(self):
        return self.birthday.value if self.birthday else TEXT["BIRTHDAY_NOT_FOUND"]

    def remove_phone(self, phone_number):
        if self.is_valid_phone_number(phone_number):
            if self.is_phone_number_exists(phone_number):
                self.phones = list(filter((lambda p: p.value != phone_number), self.phones))
                return TEXT["PHONE_NUMBER_DELETED"]
            else:
                return TEXT["PHONE_NUMBER_NOT_FOUND"]
        else:
            return TEXT["PHONE_VALIDATION"]

    def edit_phone(self, old_phone, new_phone):
        if self.is_phone_number_exists(old_phone):
            if self.is_valid_phone_number(new_phone):
                self.phones = list(map((lambda p: Phone(new_phone) if p.value == old_phone else p), self.phones))
                return TEXT["PHONE_NUMBER_UPDATED"]
            else:
                return TEXT["PHONE_VALIDATION"]
        else:
            return TEXT["PHONE_NUMBER_NOT_FOUND"]

    def find_phone(self, phone_number):
        if self.is_phone_number_exists(phone_number):
            for phone in self.phones:
                if phone.value == phone_number:
                    return phone.value
        else:
            return TEXT["PHONE_NUMBER_NOT_FOUND"]
    
    def get_string_phones(self, delimeter = ', '):
        return delimeter.join([p.value for p in self.phones]) if len(self.phones) else ""

    def find_phones(self):
        return self.get_string_phones() if len(self.phones) else TEXT["NO_DATA"]
    
    def __str__(self):
        birthday = self.birthday.value if self.birthday else "no data"
        phones = self.get_string_phones("; ") if len(self.phones) else "not data"
        return f"Contact name: {self.name.value}, phones: {phones}, birthday: {birthday}"


class AddressBook(UserDict):
    def add_record(self, contact: Record):
        self.data[contact.name.value] = contact

    def find(self, name) -> Record | None:
        return self.data.get(name, None)

    def find_all(self) -> str:
        result = ""

        if len(self.data):
            result += "\n"
            for contact in self.data.values():
                result += f"{contact}\n"
        return result

    def delete(self, name):
        removed_contact = self.data.pop(name, None)
        return TEXT["CONTACT_DELETED"] if removed_contact else TEXT["CONTACT_NOT_FOUND"]
    
    def get_birthdays_per_week(self) -> str:
        contacts_with_birthdays = list()

        for name in self.data:
            contact: Record = self.data[name]

            if contact.birthday:
                d, m, y = list(map(lambda x: int(x), contact.birthday.value.split(".")))
                contacts_with_birthdays.append({"name": name, "birthday": datetime(y, m, d)})

        return get_birthdays_per_week(contacts_with_birthdays)


def main_test():
    # Creating a new address book
    book = AddressBook()

    # Create record for John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    
    # Add and remove John phone
    john_record.add_phone("1212121212")
    john_record.remove_phone("1212121212")

    # Adding John birthday
    john_record.add_birthday("12.01.1996")

    # Adding John to the address book
    book.add_record(john_record)

    # Create and add a new record for Maxima with no phone
    maxima_record = Record("Maxima")
    maxima_record.add_birthday("18.05.2003")
    book.add_record(maxima_record)

    # Create and add a new record for Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Output of all entries in the address book
    for record in book.data.values():
        print(record)

    # Find and edit John's phone
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Output: Contact name: John, phones: 1112223333; 5555555555, birthday: 12.01.1996

    # Search for a specific phone in a John record
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Output: John: 5555555555
    found_phone = john.find_phone("7555555555")
    print(f"{john.name}: {found_phone}")  # Output: John: Phone number not found

    # Delete Jane's record
    book.delete("Jane")


if __name__ == "__main__":
    main_test()