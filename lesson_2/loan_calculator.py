# get loan_amount from user
# get APR from user as percentage
# get loan_duration in years

# compute monthly_interest_rate as (APR / 100) / 12
# compute loan_duration to months as loan_duration * 12

# compute monthly_payment with provided formula:
# m = p * (j / (1 - (1 + j) ** (-n)))

# print monthly_payment in dollars with two decimals

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
    
prompt('Welcome to The Loan Calculator!')

while True:    
    
    prompt('Please enter the total loan amount')
    loan_amount = input()

    while validate_number(loan_amount):
        prompt('Please enter a positive number')
        loan_amount = input()

    loan_amount = float(loan_amount)

    prompt('Please enter the loan duration in years.')
    loan_duration = input()
    
    while validate_number(loan_duration):
        prompt('Please enter a positive number of years')
        loan_duration = input()

    loan_duration = year_to_month(loan_duration)

    prompt('Please enter the APR as percentage. Enter 0 if no-interest loan')
    prompt('for example, enter 2 for 2%, or 5.5 for 5.5%')
    apr = input()

    while validate_percentage(apr):
        prompt('Please enter a valid percentage between 0 and 100')
        apr = input()
    
    apr = monthly_rate_calculator(float(apr))

    monthly_payment = calculate_payment(
        loan_amount,
        apr,
        loan_duration
    )

    prompt(f'Your monthly payment is ${monthly_payment:.2f}')
    
    prompt('Do you want to do another calculation? y/n')
    answer = input()
    while answer not in ['y', 'n']:
        prompt('Please answer with "y" or "n"')
        answer = input()
    if answer == 'n':
        break