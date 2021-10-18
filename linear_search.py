def linear_search(elements, target):
    for index, element in enumerate(elements):
        # Udfyldes
        if element == target:
            return index
    return None


my_list = [3, 5, 7]
print(list(enumerate(my_list)))
print(linear_search(my_list, 7))
