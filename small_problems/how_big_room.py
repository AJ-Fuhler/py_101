# Build a program that asks the user to enter the length and width of a room,
# in meters, then prints the room's area in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet

# Pseudocode:

# ask the user for the length of the room
# validate user input
# ask the user for the width of the room
# validate user input
# set square_meter variable to length * width
# set square_feet variable to square_meter * 10.7639
# return square_meter and square_feet


def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

def prompt(message):
    print(f'==> {message}')

prompt('Enter the length of the room in meters')
length = input()

while invalid_number(length):
    prompt('Please enter a valid number')
    length = input()

prompt('Enter the width of the room in meters')
width = input()

while invalid_number(width):
    prompt('Please enter a valid number')
    width = input()

square_meter = float(length) * float(width)
square_feet = square_meter * 10.7639

prompt(
    f"The room's area is {square_meter:.2f} m2 {square_feet:.2f} ft2.")