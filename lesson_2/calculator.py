import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def messages(message, lang):
    return MESSAGES[lang][message]

def prompt(message):
    print(f'==> {messages(message, language)}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

language = input("Select language: en/nl\n")
while language not in ['en', 'nl']:
    language = input("Please choose a valid language: ")

prompt('welcome')


while True:

    prompt('first_number')
    number1 = input()

    while invalid_number(number1):
        prompt('invalid_number')
        number1 = input()
    number1 = float(number1)

    prompt('second_number')
    number2 = input()

    while invalid_number(number2):
        prompt('invalid_number')
        number2 = input()
    number2 = float(number2)

    prompt('operation_type')

    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt('invalid_operation')
        operation = input()

    match operation:
        case '1':
            output = number1 + number2
        case '2':
            output = number1 - number2
        case '3':
            output = number1 * number2
        case '4':
            output = number1 / number2

    print(f"{MESSAGES[language]['result']} {output}")
    prompt('new_calculation')
    new_calculation = input()
    
    if new_calculation != MESSAGES[language]['yes']:
        break
    