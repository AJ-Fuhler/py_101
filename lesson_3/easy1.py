# 1. Will the code below raise an error?

# numbers = [1, 2, 3]
# numbers[6] = 5

# Yes, It will raise an IndexError since the numbers variable points to a list
# with only 3 objects, so index 0, 1 and 2.



# 2. How can you determine whether a given string ends with an exclamation mark
#    (!)? Write some code that prints True or False depending on whether the
#    string ends with an exclamation mark.

str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

print(str1.endswith('!'))
print(str2.endswith('!'))



# 3. Starting with the string:

famous_words = "seven years ago..."

# Show two different ways to create a new string with "Four score and "
# prepended to the front of the string.

new_string1 = "Four score and " + famous_words
new_string2  = f'Four score and {famous_words}'



# 4. Using the following string, print a string that contains the same value,
#    but using all lowercase letters except for the first character, which should
#    be capitalized.

munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'
print(munsters_description.capitalize())



# 5. print the same string with the case of all letters swapped:

print(munsters_description.swapcase())



# 6. Determine whether the name Dino appears in the strings below -- check each
# string separately:

str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

print('Dino' in str1)
print('Dino' in str2)



# 7. How can we add the family pet, "Dino", to the following list?

flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.append('Dino')



# 8. In the previous problem, our first answer added 'Dino' to the list using
#    the append method. How can we add multiple items to our list (e.g., 'Dino'
#    and 'Hoppy')? Replace the call to append with another method invocation.

flintstones.extend(["Dino", "Hoppy"])



# 9. Print a new version of the sentence given by advice that ends just before
#    the word house. Don't worry about spaces or punctuation: remove everything
#    starting from the beginning of house to the end of the sentence.

advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as

new_advice = advice.split()
print(' '.join(new_advice[:8]))
# or even cleaner:
print(advice.split("house")[0])
# splits at every occurence of "house", and returns the first element of that
# split list: Few things in life are as important as



# 10. Print the following string with the word important replaced by urgent:

advice = "Few things in life are as important as house training your pet dinosaur."

print(advice.replace('important', 'urgent'))