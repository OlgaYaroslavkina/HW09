contacts = {}


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Контакт не знайдено!"
        except ValueError:
            return "Неправильний формат вводу!"
        except IndexError:
            return "Неправильний формат команди!"

    return wrapper


@input_error
def add_contact(name, phone_number):
    contacts[name] = phone_number
    return f"Контакт {name} з номером {phone_number} успішно доданий!"


@input_error
def find_contact(name):
    return contacts[name]


@input_error
def update_contact(name, new_phone_number):
    contacts[name] = new_phone_number
    return f"Номер телефону для контакту {name} успішно оновлено!"


def show_all_contacts():
    if not contacts:
        return "Книга контактів порожня!"
    result = "Книга контактів:\n"
    for name, phone_number in contacts.items():
        result += f"{name}: {phone_number}\n"
    return result


def handle_command(command):
    if command.lower() == "hello":
        return "How can I help you?"
    elif command.lower().startswith("add"):
        try:
            _, name, phone_number = command.split(" ", 2)
            return add_contact(name, phone_number)
        except ValueError:
            return "Необхідно ввести наступні параметри: add name phone"
    elif command.lower().startswith("change"):
        try:
            _, name, phone_number = command.split(" ", 2)
            return update_contact(name, phone_number)
        except ValueError:
            return "Необхідно ввести наступні параметри: change name new_phone"
    elif command.lower().startswith("phone"):
        try:
            _, name = command.split(" ", 1)
            return find_contact(name)
        except ValueError:
            return "Необхідно ввести наступні параметри: phone name"
    elif command.lower() == "show all":
        return show_all_contacts()
    elif command.lower() in ["good bye", "close", "exit"]:
        return "Good bye!"
    else:
        return "Невідома команда. Спробуйте ще раз."


def main():
    print("Вітаємо у боті-асистенті!")

    while True:
        command = input("Введіть команду: ")
        response = handle_command(command)
        print(response)
        if response == "Good bye!":
            break


if __name__ == "__main__":
    main()