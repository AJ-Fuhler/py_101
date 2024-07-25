write out pseudocode (both casual and formal) that does the following:

1. a function that returns the sum of two numbers:

casual:

retrieve first number from user
retrieve second number from user
return first number + second number

formal:

START

GET number 1
GET number 2
PRINT number 1 + number 2

END

2. a function that takes a list of strings, and returns a string that is all
   those strings concatenated together

casual:

given a list of strings
create an empty string and save it in a variable
iterate through the collection one by one
 - for each iteration, add the current value in the list to the variable
return the variable containing all the strings concatenated.

formal:

START

Given a collection of strings called strings

SET concatString = ""

for string in strings
concatString = concatString + string

PRINT concatString

3. a function that takes a list of integers, and returns a new list with every
   other element from the original list, starting with the first element.

casual:

 given a list of integers
    create a new empty list
    set the index to 0
    iterate through the entire list
        if the number at the current index % 2 is 0
            add it to the new list
        index is index + 1
return the list
 formal:

 START

given a list of integers

SET new empty list
SET index variable to 0
WHILE index < length of list
    if number at list[index] % 2 == 0:
        add number to new list
    index is index + 1

Python:

def every_other_one(numbers):
    new_list = []
    index = 0
    while index < len(numbers):
        if number[index] % 2 == 0:
            new_list.append(numbers[index])
        index += 1
    return new_list


4. a function that determines the index of the 3rd occurrence of a given
   character in a string. For instance, if the given character is 'x' and the
   string is 'axbxcdxex', the function should return 6 (the index of the 3rd
   'x'). If the given character does not occur at least 3 times, return None.

casual:

given a string and a character

if the character is in the string at least 3 times:
    set an indexes variable to the return value of:
    loop through the string and for every matching character
     place the index of the occurrence of that character
     inside the indexes variable
     return the 3rd index of the indexes list.

formal:

START

given a string and a character

IF character's count in string >= 3:
    SET indexes variable to a list of:
    index FOR index, value in string, if the value == character
    RETURN 3rd item of indexes variable.
ELSE RETURN None

END

Python:

def index_finder(str, char):
    if str.count(char) >= 3:
        index_list = [
            index for index, character in enumerate(str) if character == char]
        return f'The 3rd occurence of {char} is at index {index_list[2]}.'   
    else:
        return None
    


5. a function that takes two lists of numbers and returns the result of merging
   the lists. The elements of the first list should become the elements at the
   even indexes of the returned list, while the elements of the second list
   should become the elements at the odd indexes. For instance:
   merge([1, 2, 3], [4, 5, 6]) # => [1, 4, 2, 5, 3, 6]


given list1 and list2

create a new list to the return value of:
    zip both lists into one list with tuples of 2 values,
    1 of each list.
    loop through the list of tuples
    loop through the tuples and add each value to the new list.
return new list

Python:

def merge(list1, list2):
    zipped_list = [
        number for element in zip(list1, list2) for number in element]
    return zipped_list


        
