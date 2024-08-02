# 1. Write two distinct ways of reversing the list without mutating the
#    original list.

numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

print(numbers[::-1])
print(list(reversed(numbers)))



# 2. Given a number and a list, determine whether the number is included in the
#    list.

numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)

print(number1 in numbers)
print(number2 in numbers)



# 3. Programmatically determine whether 42 lies between 10 and 100, inclusive.
#    Do the same for the values 100 and 101.

print(42 in range(10, 101))
print(100 in range(10, 101))
print(101 in range(10, 101))