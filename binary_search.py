# Implementering af binær søgning
import math

def binary_search(elements, target):
    n = len(elements)
    L = 0
    R = n - 1
    while L <= R:
        m = math.floor((L+R)/2)
        if elements[m] < target:
            L = m + 1
        elif elements[m] > target:
            R = m - 1
        else:
            return m
    return None


test_list = [2, 3, 5, 7, 11]
print(binary_search(test_list, 2))
print(binary_search(test_list, 7))
print(binary_search(test_list, 11))
print(binary_search(test_list, 5))
