Homework consists of 2 tasks

# Task 1. Refine the helper console Bot and add error handling.

## Description

File name `bot.py`. The file contains a main function and be called dirrectly from the console `python bot.py`.

## What was done

Added improved **input_error** decorator for following methods: `change_contact`, `add_contact`, `show_phone`. It takes an error message as an argument and return one as a message if an exception was caught.

Examples of the use:

```
@input_error("Give me name and phone please.")
def change_contact(args, contacts):
```

_function expects two arguments: **name** and **phone number**_

or

```
@input_error("Give me name please.")
def show_phone(args, contacts):
```

_function expects only one argument: **name**_

## How to run

Example of the Bot call:

```
python bot.py
```

In order to terminate the Bot use "close" or "exit" command.

```
Enter a command: close
Good bye!
```

## Modules

The folder `bot_utils` contains all the important utilities for the Bot to work.

# Task 2. Develop a system for managing the address book.

## Description

File name `address_book.py`. The file contains a main function with testing implementation and be called dirrectly from the console `python address_book.py`.

## How to run

Example of the use manually:

**Creating a new address book**

```
book = AddressBook()
```

**Creating a record for John**

```
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
```

**Adding John to the address book**

```
book.add_record(john_record)
```

**Output of all entries in the address book**

```
for name, record in book.data.items():
    print(record)
```

**Find and edit John's phone**

```
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Output: Contact name: John, phones: 1112223333; 5555555555
```

**Search for a specific phone in a John record**

```
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Output: 5555555555
```

**Deleting Jane's record**

```
book.delete("Jane")
```

## Modules

No extra modules.

# Extra files in the project not related to the current Homework

## get_birthdays_per_week.py

The file contains a function `get_birthdays_per_week` that's called with a list of dictionaries. Each dictionary must have such required keys as `name` and `birthday`.

Example of a dictionary:

```
{"name": "Bill Gates", "birthday": datetime(1955, 11, 11)}
```

The function `get_birthdays_per_week`` outputs the names of birthday people in the following format:

```
Monday: Bill Gates, Jill Valentine
Friday: Kim Kardashian, Jan Koum
```

### How to run

Example of the function call:

```
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 11, 11)},
    {"name": "Jill Valentine", "birthday": datetime(1955, 11, 12)},
    {"name": "Kim Kardashian", "birthday": datetime(1955, 11, 10)},
    {"name": "Jan Koum", "birthday": datetime(1955, 11, 10)},
]

get_birthdays_per_week(users)

```
