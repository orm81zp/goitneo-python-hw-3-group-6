# It's time to combine our previous homework into one.

## Description

File name `main.py`. The file runs The Assistant Bot.
The project contains the **assistant_bot** module, which exports the `run_bot` function.

## How to run

Examples of the use:

```
from assistant_bot import run_bot

def main():
    run_bot()


if __name__ == "__main__":
    main()
```

or directly from the terminal `python main.py`

In order to close the program use `close` or `exit` command.

```
Enter a command: close
Good bye!
```

Below is a list of available commands with examples of usage:

```
add                 used to add a phone number: "add [username] [phone]"
remove              used to remove a phone number: "remove [username] [phone]"
change              used to change a phone number: "change [username] [phone]"
phone               used to display a phone number(s): "phone [username]"
all                 used to display all contacts: "all"
add-birthday        used to add a birthday: "add-birthday [username] [birthday]"
show-birthday       used to display a birthday: "show-birthday [username]"
birthdays           used to display birthdays that will happen in the next week: "birthdays"
remove-contact      used to remove a contact: "remove-contact [username]"
hello               used to display a welcome message: "hello"
close or exit       used to close the program: "exit"
help                used to display available commands: "help"
```

### add

Used to add a phone number: `add [username] [phone]`

```
Enter a command: add John 0970000001
Phone number added.
Enter a command: add John 0630000001
Phone number added.
Enter a command: add Erik 0660000001
Phone number added.
```

### add-birthday

Used to add a birthday: `add-birthday [username] [birthday]`

```
Enter a command: add-birthday John 28.11.2001
Birthday added.
```

### show-birthday

Used to display a birthday: `show-birthday [username]`

```
Enter a command: show-birthday John
28.11.2001
```

### remove-contact

Used to remove a contact: `remove-contact [username]`
Considering that this is a not safe command, you need to confirm your intention with "yes" or "y".

```
Enter a command: remove-contact Erik
Are you sure you want to delete the contact (y or n)? y
Contact deleted
```

### all

Used to display all contacts: `all`

```
Enter a command: all
Contact name: John, phones: 0970000001; 0630000001

```

### change

Used to change a phone number: `change [username] [phone]`

```
Enter a command: change John 0630000001 0730000001
Phone number updated.

```

### phone

Used to display a phone number: `phone [username]`

```
Enter a command: phone John
0970000001, 0730000001
```

### remove

Used to remove a phone number: `remove [username] [phone]`

```
Enter a command: remove John 0970000001
Phone number deleted.
Enter a command: phone John
0730000001

```

### birthdays

Used to display birthdays that will happen in the next week: `birthdays`

The example of the output:

```
Monday: Bill Gates, Jill Valentine
Friday: Kim Kardashian, Jan Koum

```

Let's assume that today is 26.11.2023 (Sunday) and run the `birthdays` command. Just a small reminder that John's birthday is 28.11.2001.

```
Enter a command: birthdays
Tuesday: John
```

## Modules

The folder `assistant_bot` contains all the important utilities for the Bot to work.

# Additional functionality of saving and restoring the contacts.

## Description

The project contains the **assistant_bot** module, which exports the `run_bot` function.
The function can take an optional **dump_file_path** parameter that specifies the path to a dump file to save data when the program closes.
If `dump_file_path` is not specified, the `assistant_bot_data.bin` default file will be used alongside the main.py file.

### Close the programm

use `close` or `exit` to close the program.

```
Enter a command: exit
Good bye!
```

if there are any contacts already available then a dump file will be created alongside the main.py file after closing the program. The dump file is used to recover contacts.

To empty your contacts just delete the dump file.
