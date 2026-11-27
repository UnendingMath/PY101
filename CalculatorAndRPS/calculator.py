import json

def prompt(key):
    print(f"==> {MESSAGES[language][key]}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def prompt_number(prompt_key):
    prompt(prompt_key)
    number = input()
    while invalid_number(number):
        prompt('invalid_number')
        number = input()
    return number

def invalid_operation(prompt_key):
    prompt(prompt_key)
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt('invalid_operation')
        operation = input()

    return operation

def evaluate_operation(num1, num2, operation):
    match operation:
        case '1':
            return round(float(num1) + float(num2), 2)
        case '2':
            return round(float(num1) - float(num2), 2)
        case '3':
            return round(float(num1) * float(num2), 2)
        case '4':
            try:
                return round(float(num1), 2) / round(float(num2), 2)
            except ZeroDivisionError:
                prompt('divide_by_zero')
                return 0


with open("calculator_messages.json", "r", encoding="utf-8") as file:
    MESSAGES = json.load(file)

print(f"==> {MESSAGES["language"]['welcome']}")
language = input()

while language not in ['1', '2']:
    print(f"==>{MESSAGES["language"]["invalid_language"]}")
    language = input()

match language:
    case "1":
        language = "english"
    case "2":
        language = "spanish"

while True:

    number1 = prompt_number('first_number')
    number2 = prompt_number('second_number')
    chosen_operation = invalid_operation('operation')
    output = evaluate_operation(number1, number2, chosen_operation)

    print(f"==> {MESSAGES[language]['result']}{output}")

    prompt("another")
    another = input().strip().lower()

    if another and another[0] != "y":
        break