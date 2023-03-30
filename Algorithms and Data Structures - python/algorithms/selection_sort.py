def selection_sort(numbers):

    sorted_list = []
    #print("%-25s  %-25s" % (numbers, sorted_list))
    for i in range(len(numbers)):
    
        index_move = index_of_min(numbers)
        sorted_list.append(numbers.pop(index_move))
        print("%-25s  %-25s" % (numbers, sorted_list))
    
    return sorted_list

def index_of_min(numbers):
    
    index_of_min = 0

    for i in range(1, len(numbers)):

        if numbers[i] < numbers[index_of_min]:
            index_of_min  = i
    return index_of_min


if __name__=='__main__':
    selection_sort([5,8,1,4,7,52,64,21,11])
        