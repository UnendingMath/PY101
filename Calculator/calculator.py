import json

def prompt(text):
    print(f"==> {text}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

with open("calculator_messages.json", "r", encoding="utf-8") as file:
    MESSAGES = json.load(file)

while True:
    prompt(MESSAGES['welcome'])

    prompt(MESSAGES['first_number'])
    number1 = input()

    while invalid_number(number1):
        prompt(MESSAGES['invalid_number'])
        number1 = input()

    prompt(MESSAGES['second_number'])
    number2 = input()

    while invalid_number(number2):
        prompt(MESSAGES['invalid_number'])
        number2 = input()

    prompt(MESSAGES['operation'])
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(MESSAGES['invalid_operation'])
        operation = input()

    match operation:
        case '1':
            output = int(number1) + int(number2)
        case '2':
            output = int(number1) - int(number2)
        case '3':
            output = int(number1) * int(number2)
        case '4':
            output = int(number1) / int(number2)

    print(f"{MESSAGES['result']}{output}")

    prompt(MESSAGES["another"])
    another = input()

    if another and another.strip().lower()[0] != "y":
        break