

def quicksort(numbers):
    ## base case
    if (len(numbers) <= 1):
        return numbers ## in case [] or [a]
    pivot = numbers[0]
    less_than_pivot = []
    greater_than_pivot = []

    for value in numbers[1:]: #excluding pivot
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

if __name__=='__main__':

    print(quicksort([5,8,1,4,7,52,64,21,11]))