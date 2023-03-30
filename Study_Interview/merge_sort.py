
## Divide and Conquer

def merge_sort(list):
    """
    Sorts list in ascending order returns new sorted list
    Divide: find midpoint in list and divide into sublists
    Conquer: Recursively sort the sublist created in previous step
    Combine: Merge sortes sublists
    O(n log n)
    """
    """ 
    time: O(n*log(n))
    """
    if len(list) <= 1:
        return list

    left_half, right_half = split(list) ## split is not written yet
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide unsorted list at midpoint into 2 sublists
    Takes O(log n) time
    Slicing is a O(k log n) overall 
    """
    midpoint = len(list)//2
    
    left = list[:midpoint] ## does not include midpoint
    right = list[midpoint:] ## includes midpoint

    return left, right



def merge(left, right):
    ## merges two lists (arrays), 
    ## sorting them in the process
    ## O(n*log n) n halves and n number of steps
    l = []
    i,j = 0,0 ## indexes: left, right
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    while i < len(left):
        l.append(left[i])
        i += 1
    while j < len(right):
        l.append(right[j])
        j += 1

    return l

def verify_sorted(list):

    if len(list) == 0 or len(list) == 1:
        return True
    ## recursion instead of loop
    return list[0] < list[1] and verify_sorted(list[1:])
    

if __name__ == '__main__':

    alist = [54,62,93,17,77,31,44,55,20]
    l = merge_sort(alist)
    print(l)
    print(verify_sorted(l))

