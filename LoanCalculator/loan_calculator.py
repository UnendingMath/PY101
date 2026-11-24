import json

MONTHS_IN_YEAR = 12
MAKE_A_PERCNTAGE = 100

def prompt(language, key):
    print(f"==> {MESSAGES[language][key]}")

def invalid_input(number):
    try:
        result = float(number)
        if result < 0:
            return True 
        return False
    except ValueError:
        return True

def check_number(language, number):
    while invalid_input(number):
        prompt(language, 'invalid_number')
        number = input().strip()
    return float(number)

def obtain_language():
    prompt('welcome', 'question')
    while True:
        language = input().strip()
        match language:
            case "1":
                return "english"
            case "2":
                return "spanish"
            case _:
                print("Please enter a valid language option.")

def obtain_loan_amount():
    prompt(language, 'loan_amount')
    loan_amount = check_number(language, input().strip())
    while loan_amount == 0:
        prompt(language, 'invalid_number')
        loan_amount = check_number(language, input().strip())
    return loan_amount

def obtain_monthly_apr():
    prompt(language, 'apr_amount')
    apr = input().strip()
    return check_number(language, apr) / MAKE_A_PERCNTAGE / MONTHS_IN_YEAR

def obtain_monthly_duration():
    prompt(language, 'duration_amount')
    duration = check_number(language, input().strip())

    while duration == 0:
        prompt(language, 'invalid_number')
        duration = check_number(language, input().strip())

    return duration * MONTHS_IN_YEAR

def calc_monthly_payment(total_loan, rate, duration):
    try:
        return total_loan * (rate / (1 - (1 + rate) ** (-duration)))
    except ZeroDivisionError:
        return total_loan / duration
    
            
with open('loan_messages.json', 'r') as file:
    MESSAGES = json.load(file)

# Obtain Language
language = obtain_language()

while True:

    # Obtain Total Amount
    loan_amount = obtain_loan_amount()

    # Obtain APR
    monthly_rate = obtain_monthly_apr()

    # Obtain Duration
    duration_months = obtain_monthly_duration()

    # Calculate Monthly Payment
    monthly_payment = calc_monthly_payment(loan_amount, monthly_rate, duration_months)

    print(f"""
==> Loan Amount: {loan_amount:.2f}
==> APR: {monthly_rate * MAKE_A_PERCNTAGE * MONTHS_IN_YEAR}%
==> Duration: {duration_months / MONTHS_IN_YEAR} years

==> Your monthly payment is: ${monthly_payment:.2f}
    """)


    prompt(language, "another_calc")
    answer = input().strip().lower()
    if answer and answer[0] != "y":
        break
    
    