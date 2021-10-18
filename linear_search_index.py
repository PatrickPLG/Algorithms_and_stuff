# Implementering af lineær søgning i liste via index


def linear_search(elements, target):
    n = len(elements)
    R = n - 1
    m = 0
    while m <= R:
        if elements[m] == target:
            return m
        elif elements[m] < target:
            m = m + 1
        elif elements[m] > target:
            return None


#test_list = [3, 11, 5, 2, 7]
test_list = [2,3,5,7,11]
print(linear_search(test_list, 2))
print(linear_search(test_list, 7))
print(linear_search(test_list, 11))
print(linear_search(test_list, 5))
