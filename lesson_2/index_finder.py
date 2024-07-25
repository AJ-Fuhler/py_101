def index_finder(str, char):
    if str.count(char) >= 3:
        index_list = [
            index for index, character in enumerate(str) if character == char]
        return f'The 3rd occurence of {char} is at index {index_list[2]}.'   
    else:
        return None
    
print(index_finder('axbxcdxex', 'x'))




