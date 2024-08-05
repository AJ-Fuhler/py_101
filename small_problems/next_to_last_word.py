def penultimate(str):
    if str.strip() == '':
        return 'That was an empty string you entered there.'
    word_list = str.strip().split()
    if len(word_list) == 1:
        return word_list[0]
    elif len(word_list) == 2:
        return 'No middle word when you enter a 2 word string'
    elif len(word_list) % 2 == 1:
        return word_list[len(word_list) // 2]
    else:
        return f'{word_list[(len(word_list) - 1) // 2]}, {word_list[len(word_list) // 2]}'


# These examples should print True
print(penultimate("last word"))
print(penultimate("Launch School is super duper great!"))