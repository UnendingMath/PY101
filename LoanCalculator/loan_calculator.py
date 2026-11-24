import json

MONTHS_IN_YEAR = 12
MAKE_A_PERCNTAGE = 100

def prompt(lan, key):
    print(f"==> {MESSAGES[lan][key]}")

def invalid_input(number):
    try:
        result = float(number)
        if result < 0:
            return True
        return False
    except ValueError:
        return True

def check_number(lan, number):
    while invalid_input(number):
        prompt(lan, 'invalid_number')
        number = input().strip()
    return float(number)

def obtain_language():
    prompt('welcome', 'question')
    while True:
        lan = input().strip()
        match lan:
            case "1":
                return "english"
            case "2":
                return "spanish"
            case _:
                print("Please enter a valid LANGUAGE option.")

def obtain_loan_amount():
    prompt(LANGUAGE, 'loan_amount')
    amount = check_number(LANGUAGE, input().strip())
    while amount == 0:
        prompt(LANGUAGE, 'invalid_number')
        amount = check_number(LANGUAGE, input().strip())
    return amount

def obtain_monthly_apr():
    prompt(LANGUAGE, 'apr_amount')
    apr = input().strip()
    return check_number(LANGUAGE, apr) / MAKE_A_PERCNTAGE / MONTHS_IN_YEAR

def obtain_monthly_duration():
    prompt(LANGUAGE, 'duration_amount')
    duration = check_number(LANGUAGE, input().strip())

    while duration == 0:
        prompt(LANGUAGE, 'invalid_number')
        duration = check_number(LANGUAGE, input().strip())

    return duration * MONTHS_IN_YEAR

def calc_monthly_payment(total_loan, rate, duration):
    try:
        return total_loan * (rate / (1 - (1 + rate) ** (-duration)))
    except ZeroDivisionError:
        return total_loan / duration


with open('loan_messages.json', 'r') as file:
    MESSAGES = json.load(file)

# Obtain Language
LANGUAGE = obtain_language()

while True:

    # Obtain Total Amount
    principal = obtain_loan_amount()

    # Obtain APR
    monthly_rate = obtain_monthly_apr()

    # Obtain Duration
    months = obtain_monthly_duration()

    # Calculate Monthly Payment
    monthly_payment = calc_monthly_payment(principal, monthly_rate, months)

    print(f"""
==> Loan Amount: {principal:.2f}
==> APR: {monthly_rate * MAKE_A_PERCNTAGE * MONTHS_IN_YEAR}%
==> Duration: {months / MONTHS_IN_YEAR} years

==> Your monthly payment is: ${monthly_payment:.2f}
    """)


    prompt(LANGUAGE, "another_calc")
    answer = input().strip().lower()
    if answer and answer[0] != "y":
        break
