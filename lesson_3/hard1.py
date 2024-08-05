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
