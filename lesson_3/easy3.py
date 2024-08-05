# 1. Write two different ways to remove all of the elements from the following
#    list:

numbers = [1, 2, 3, 4]
numbers.clear()

# for number in numbers:
#    number.pop()

# or: while number:
#         numbers.pop()



# 2. What will the following code output?

print([1, 2, 3] + [4, 5]) # [1, 2, 3, 4, 5]



# 3. What will the following code output?

str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1) # hello there



# 4. What will the following code output?

my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1) # [{"first": "42"}, {"second": "value2"}, 3, 4, 5]

# This is because we made a shallow copy of my_list1, and shallow copies only
# make duplicates of the outermost values in an object. The nested objects in a
# collection are just pointers to the memory location for that nested object.
# the pointer (or reference) gets copied. Thus, nested objects in list_1 and
# list_2 reference the same object in memory elsewhere.



# 5. The following function unnecessarily uses two return statements to return
#    boolean values. Can you rewrite this function so it only has one return
#    statement and does not explicitly use either True or False?

def is_color_valid(color):
    return color == "blue" or color == "green"

def is_color_valid(color):
    return color in ['green', 'blue']
      