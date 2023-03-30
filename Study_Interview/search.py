### Linear Search Algorithm


def data_from_file(test_file):
    # input: file_name in directory
    # output: list with index-line data on file
    with open(test_file, 'r', encoding='utf8') as reader:
        sample = []
        for line in reader:
            sample.append(float(line.strip()))
    return sample

def data_to_file(test_file, data):
    # input: data to upload in file
    # output: file in directory with list's data each line for each index
    with open(test_file, 'w', encoding='utf8') as writer:
        for line in writer:
            writer.write(data)

    return "Done!"

    

def linear_search(value, data_list):
        ## We will go 1 to 1 in each value in self.data_list
        ## if we find value in data_list then return index
    for index in range(len(data_list)):
        if value == data_list[index]:
            return index
        
def binary_search(value, data_list):
    first = 0
    last = len(data_list) - 1

    while first <= last:
        midpoint_index = (last + first)//2 
        
        if data_list[midpoint_index] == value:
            return midpoint_index
        elif data_list[midpoint_index] < value:
            first = midpoint_index + 1
        else: 
            last = midpoint_index - 1

    return None

def binary_search_recursive(value, data_list):
## if we slice the list, then the index will not be found
## this implementation only returns True if value is in data_list
    if len(data_list) == 0:
        return False
    else:
        mid = len(data_list)//2
        if (value == data_list[mid]):
            return True
        else:
            if value > data_list[mid]:
                return binary_search_recursive(value,data_list[mid+1:])
            else:
                return binary_search_recursive(value,data_list[:mid])


if __name__=='__main__':

    unsorted = [0,1,2,3,4,5,7,8,9,11,13,20,52,53,55,59]#[5,8,1,4,7,52,64,21,11]
    sorted = [0,1,2,3,4,5,7,8,9,11,13,20,52,53,55,59]
    
    #print(linear_search(52, unsorted))
    #print(linear_search(52, sorted))
    print(binary_search(59, sorted))
    print(binary_search_recursive(59, sorted))



