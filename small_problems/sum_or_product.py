# Write a program that asks the user to enter an integer greater than 0, then
# asks whether the user wants to determine the sum or the product of all
# numbers between 1 and the entered integer, inclusive.

# define a function that returns the sum of a given integer
# define a function that returns the product of a given integer

# assign prompt_1 variable to string asking for integer greater than 0
# assign prompt_2 variable to string asking to compute sum 's' or product 'p'

# set number variable to user input with prompt_1 string
# validate that number variable can be coerced to integer

# set operation variable to user input with prompt_2 string
# validate that operation variable is either 's' or 'p'

# IF operation is 's':
#   SET result variable to the return value of sum_function(number)
#   PRINT result in string
#
# ELSE:
#   SET result variable to the return value of product_function(number)
#   PRINT result in string

def compute_sum(num):
    return sum(range(1, num + 1))

def compute_product(num):
    result = 1
    for value in range(2, int(num) + 1):
        result *= value
    return result

PROMPT_1 = 'Please enter an integer greater than 0: '
PROMPT_2 = 'Enter "s" to compute the sum, or "p" to compute the product. '

number = input(PROMPT_1)

while not number.isdigit():
    number = input('Please enter a valid integer greater than 0: ')

number = int(number)

while number <= 0:
    number = input('Please enter a valid integer greater than 0: ')


operation = input(PROMPT_2)

while operation not in ('s', 'p'):
    operation = input("Please enter 's' or 'p': ")

if operation == 's':
    print(
        f'The sum of the integers between 1 and {number} '
        f'is {compute_sum(number)}.')
else:
    print(f'The product of the integers between 1 and {number} '
          f'is {compute_product(number)}.')