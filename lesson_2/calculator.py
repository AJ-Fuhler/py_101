import json
import os
import math

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def messages(message, lang):
    return MESSAGES[lang][message]

def prompt(message):
    print(f'==> {messages(message, language)}')

def invalid_number(number_str):
    try:
        float(number_str)
        if math.isnan(number_str):
            raise ValueError
    except ValueError:
        return True
    return False

def get_language():
    lang = input("Select language: en/nl\n").lower()
    while lang not in ['en', 'nl']:
        lang = input("Please choose a valid language: ")
    return lang

def get_number():
    number = input()
    while invalid_number(number):
        prompt('invalid_number')
        number = input()
    return float(number)

def get_operation():
    oper = input()
    while oper not in ['1', '2', '3', '4']:
        prompt('invalid_operation')
        oper = input()

    return oper

def get_choice():
    choice = input()
    while choice not in ['1', '2']:
        prompt('invalid_choice')
        choice = input()
    return choice

def catch_zero_division(num, oper):
    while num == 0 and oper == '4':
        prompt('zero_division')
        choice = get_choice()
        if choice == '1':
            prompt('second_number')
            num = get_number()
        else:
            prompt('operation_type')
            oper = get_operation()

    return num, oper


def perform_operation(num1, num2, oper):
    if num2 == 0 and oper == '4':
        num2, oper = catch_zero_division(num2, oper)

    match oper:
        case '1':
            result = num1 + num2
        case '2':
            result = num1 - num2
        case '3':
            result = num1 * num2
        case '4':
            result = num1 / num2

    return result

language = get_language()

while True:
    os.system('clear')
    prompt('welcome')
    prompt('first_number')
    number1 = get_number()

    prompt('second_number')
    number2 = get_number()

    prompt('operation_type')
    operation = get_operation()
    output = perform_operation(number1, number2, operation)

    print(f"{MESSAGES[language]['result']} {output}")
    prompt('new_calculation')
    new_calculation = input().lower()
    if new_calculation != MESSAGES[language]['yes']:
        break