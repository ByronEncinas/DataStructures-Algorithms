## Randomizes the order of list until sorted

import random


numbers = [5,8,1,4,7,52,64,21,11]

print(numbers)

def is_sorted(values):
    for index in range(len(values)-1):
        if values[index] > values[index+1]:
            return False
    return True

def bogo_sort(values):
    attemps = 0
    while not is_sorted(values):
        random.shuffle(values)
        attemps +=1
        print(attemps)
    return values

print(bogo_sort(numbers))