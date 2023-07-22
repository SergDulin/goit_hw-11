from clphone import *

address_book = AddressBook()

@input_error
def add(*args):
    if len(args) < 2:
        raise ValueError("Please provide both name and phone number")

    name = Name(args[0])
    phones = []
    birthday = None

    for arg in args[1:]:
        if arg.startswith("+380"):
            phones.append(Phone(arg))
        elif arg.count(".") == 2:
            birthday = Birthday(arg)
        else:
            name.value += " " + arg

    rec = address_book.data.get(str(name))
    if rec:
        for phone in phones:
            rec.add_phone(phone)
        if birthday:
            rec.birthday = birthday
    else:
        rec = Record(name)
        rec.birthday = birthday
        for phone in phones:
            rec.add_phone(phone)
        address_book.add_record(rec)
    return f"Contact {name}: {', '.join(str(num) for num in rec.phones)}{', ' + str(rec.birthday) if rec.birthday else ''} added successfully"

@input_error
def change(*args):
    if len(args) != 3:
        raise ValueError("Please provide the name, old phone number, and new phone number")

    name = Name(args[0])
    old_phone = Phone(args[1])
    new_phone = Phone(args[2])

    rec = address_book.data.get(str(name))
    if rec:
        rec.change_phone(old_phone, new_phone)
    else:
        raise KeyError(f"Contact '{name}' not found in address book")

    return f"Old phone {old_phone} changed to {new_phone}"

@input_error
def phone(*args):
    if len(args) != 1:
        raise ValueError("Please provide the name")

    keyword = args[0].capitalize()

    matches = []
    for record in address_book:
        if keyword in str(record.name).capitalize():
            matches.append(record)

    result = ""
    if matches:
        for record in matches:
            result += str(record) + "\n"
    else:
        raise KeyError(f"Contact '{keyword}' not found in address book")
    return result

@input_error
def show_all(*args):
    if not address_book.data:
        return "There are no contacts saved."

    result = ""
    for record in address_book:
        result += str(record) + "\n"

    return result

def hello_command(*args):
    return "How can I help you?"

def goodbye_command(*args):
    return "Goodbye!"

def no_command(*args):
    return "Invalid command. Please try again."

command_handlers = {
    add: ("add",),
    change: ("change",),
    phone: ("phone",),
    show_all: ("show all",),
    hello_command: ("hello",),
    goodbye_command: ("good bye", "close", "exit")
}

def komand(user_input):
    for command, keywords in command_handlers.items():
        for keyword in keywords:
            if user_input.lower().startswith(keyword):
                return command, user_input[len(keyword):].strip().split()
    return no_command, []

def main():
    while True:
        user_input = input("Enter a command: ")
        func, data = komand(user_input)
        print(func(*data))
        if func == goodbye_command:
            break

if __name__ == "__main__":
    main()