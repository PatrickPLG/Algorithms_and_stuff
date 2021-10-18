def my_sum(number):
    biggest = number[0]
    for x in number:
        if x > biggest:
            biggest = x
    return biggest

print(my_sum([-50,-1123200,-22310,-1000,-213]))