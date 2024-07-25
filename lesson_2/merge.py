def merge(list1, list2):
    zipped_list = [
        number for element in zip(list1, list2) for number in element]
    return zipped_list

    

print(merge([1, 2, 3], [4, 5, 6]))