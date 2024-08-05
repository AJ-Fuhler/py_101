# Create a function that takes two arguments, multiplies them together, and
# returns the result.

def multiply(num1, num2):
    return num1 * num2

print(multiply(5, 3) == 15)  # True

def square(num):
    return multiply(num, num)

print(square(5) == 25)   # True
print(square(-8) == 64)  # True

def power(num, exponant):
    result = 1
    for _ in range(exponant):
        result = multiply(result, num)
    return result

print(power(3, 3))