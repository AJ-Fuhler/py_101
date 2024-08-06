# 1. Will the following functions return the same results?

def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())

# No, second will only return None. The opening curly brace should have been on
# the same line as the return statement.



# 2. What does the last line in the following code output?

dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)
print(dictionary)

# {'first': [1, 2]} num_list is a reference to the original list in the
# dictionary. Because of this, using the append method, mutates the original
# list.

# instead, if you only want to modify num_list, you can either do:
num_list = dictionary['first'].copy()
num_list.append(2)

# or use list slicing which returns a new list:

num_list = dictionary['first'][:]
num_list.append(2)


# 3. Given the following similar sets of code, what will each code snippet
#    print?

# A
def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}") # one is: ["one"]
print(f"two is: {two}") # two is: ["two"]
print(f"three is: {three}") # three is: ["three"]


# B
def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}") # one is: ["one"]
print(f"two is: {two}") # two is: ["two"]
print(f"three is: {three}") # three is: ["three"]


# C
def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}") # one is: ["two"]
print(f"two is: {two}") # two is: ["three"]
print(f"three is: {three}") # three is: ["one"]



# 4. Ben was tasked to write a simple Python function to determine whether an
#    input string is an IP address using 4 dot-separated numbers, e.g.,
#    10.4.5.11.

# Alyssa supplied Ben with a function named is_an_ip_number. It determines
# whether a string is a numeric string between 0 and 255 as required for IP
# numbers and asked Ben to use it. Here's the code that Ben wrote:

# Alyssa reviewed Ben's code and said, "It's a good start, but you missed a few
# things. You're not returning a false condition, and you're not handling the
# case when the input string has more or less than 4 components, e.g., 4.5.5 or
# 1.2.3.4.5: both those values should be invalid."

# Help Ben fix his code.

def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False
    
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True


# 5. What do you expect to happen when the greeting variable is referenced in
#    the last line of the code below?

if False:
    greeting = "hello world"

print(greeting) # NameError. if block is not executed due to False condition.
