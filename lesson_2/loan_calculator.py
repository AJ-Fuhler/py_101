import os

def prompt(message):
    print(f'==> {message}')

def monthly_rate_calculator(rate):
    return (float(rate) / 100) / 12

def year_to_month(year):
    return float(year) * 12

def validate_number(num):
    try:
        number = float(num)
        if number < 0:
            raise ValueError
    except ValueError:
        return True
    return False

def validate_percentage(percentage):
    while validate_number(percentage):
        prompt('Please enter a valid percentage between 0 and 100')
        percentage = input()
    return not (float(percentage) >= 0 and float(percentage) <= 100)

def calculate_payment(amount, rate, duration):
    return amount * (rate / (1 - (1 + rate) ** (-duration)))

def get_loan_amount():
    amount = input()
    while validate_number(amount):
        prompt('Please enter a positive number')
        amount = input()

    return float(amount)

def get_loan_duration():
    duration = input()
    while validate_number(duration):
        prompt('Please enter a positive number of years')
        duration = input()

    return year_to_month(duration)

def get_apr():
    rate = input()
    while validate_percentage(rate):
        prompt('Please enter a valid percentage between 0 and 100')
        rate = input()
    return monthly_rate_calculator(float(rate))

prompt('Welcome to The Loan Calculator!')

while True:
    prompt('Please enter the total loan amount')
    loan_amount = get_loan_amount()

    prompt('Please enter the APR as percentage. Enter 0 if no-interest loan')
    prompt('for example, enter 2 for 2%, or 5.5 for 5.5%')
    apr = get_apr()
    prompt('Please enter the loan duration in years.')
    loan_duration = get_loan_duration()
    monthly_payment = calculate_payment(
        loan_amount,
        apr,
        loan_duration
    )

    prompt(f'Your monthly payment is ${monthly_payment:.2f}')
    prompt('Do you want to do another calculation? y/n')
    answer = input().lower()
    while answer not in ['y', 'n']:
        prompt('Please answer with "y" or "n"')
        answer = input().lower()
    if answer == 'n':
        break
    os.system('clear')