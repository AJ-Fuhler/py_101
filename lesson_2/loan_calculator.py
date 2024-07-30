import os
import math

def prompt(message):
    print(f'==> {message}')

def calculate_monthly_rate(rate):
    return (float(rate) / 100) / 12

def year_to_month(year):
    return float(year) * 12

def validate_number(num):
    try:
        number = float(num)
        if number <= 0 or math.isnan(number):
            raise ValueError
    except ValueError:
        return True

    return False

def validate_zero_greater(num):
    try:
        number = float(num)
        if number < 0 or math.isnan(number):
            raise ValueError
    except ValueError:
        return True

    return False

def validate_percentage(percentage):
    while validate_zero_greater(percentage):
        prompt('Please enter a valid percentage between 0 and 100')
        percentage = input()

    return not (float(percentage) >= 0 and float(percentage) <= 100)

def calculate_payment(amount, rate, duration):
    if rate == 0:
        return amount / duration
    return amount * (rate / (1 - (1 + rate) ** (-duration)))

def get_loan_amount():
    prompt('Please enter the total loan amount')
    amount = input()

    while validate_number(amount):
        prompt('Please enter a positive number')
        amount = input()

    return float(amount)

def get_loan_duration():
    prompt('Please enter the loan duration in years.')
    duration = input()

    while validate_number(duration):
        prompt('Please enter a positive number of years')
        duration = input()

    return year_to_month(duration)

def get_apr():
    prompt('Please enter the APR as percentage. Enter 0 if no-interest loan')
    prompt('for example, enter 2 for 2%, or 5.5 for 5.5%')
    rate = input()

    while validate_percentage(rate):
        prompt('Please enter a valid percentage between 0 and 100')
        rate = input()

    return calculate_monthly_rate(float(rate))

def display_results(payment_amount):
    prompt(f'Your monthly payment is ${payment_amount:.2f}')

def calculate_again():
    prompt('Do you want to do another calculation? y/n')
    answer = input().lower()

    while answer not in ['y', 'n']:
        prompt('Please answer with "y" or "n"')
        answer = input().lower()
    return answer

def display_welcome_prompt():
    prompt('Welcome to The Loan Calculator!')

while True:
    os.system('clear')
    display_welcome_prompt()
    loan_amount = get_loan_amount()
    apr = get_apr()
    loan_duration = get_loan_duration()
    monthly_payment = calculate_payment(loan_amount, apr, loan_duration)
    display_results(monthly_payment)
    calculate_again_answer = calculate_again()
    if calculate_again_answer == 'n':
        break