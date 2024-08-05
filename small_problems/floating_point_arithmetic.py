def calculate(num1, num2, operation):
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2
        case '//':
            return num1 // num2
        case '%':
            return num1 % num2
        case '**':
            return num1 ** num2
        
first_number = float(input("==> Enter the first number:\n"))
second_number = float(input("==> Enter the second number:\n"))

for operator in ['+', '-', '*', '/', '//', '%', '**']:
    operation = f"==> {first_number} {operator} {second_number}"
    print(f"{operation} = {calculate(first_number, second_number, operator)}")
