## how runtime is affected by a data structure
from linked_list import LinkedList

""" l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
print(l) """


def merge_sort(linked_list):
    ## sorts linked list in asc. order
    # -- recursively divide linked into sublists containing single node
    # -- repeatedly merge the sublists to produce sorted sublists untile one remians
    # Returns sortes linked list
    # O(k * n * log n)

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right)

def split(linked_list):
    """ 
    Divide unsorted at midpoint into sublists
    O(k log n)
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2
        mid_node = linked_list.node_at_index(mid-1)
        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half

def merge(left, right):
    """ 
    Merges two linked list, sorting by data in the nodes, 
    and returns new, merged list
    """
    # Create a new linked list containing nodes from 
    # merging left and right
    merged = LinkedList()

    # Add fake head to delete later
    merged.add(0)

    ## Set current to the head of the linked list
    current = merged.head

    # Obtain head nodes for both left and right
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until reach tail node of either
    while left_head or right_head:
        ## if head node of left is None, we past tail
        ## Add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            right_head = right_head.next_node
        # If the head node of right is None, we're past the tail
        # Add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            
            left_head = left_head.next_node
        else: 
            # Not at either tail node
            # obtein node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            # if data on left is less than right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node
            # Move current to next node
        current = current.next_node
    # Discard fake head
    head = merged.head.next_node
    merged.head = head

    return merged

## try verify function              

if __name__ == '__main__':

    l = LinkedList()
    l.add(10)
    l.add(2)
    l.add(44)
    l.add(15)
    l.add(200)
    print(l.head, l.head.next_node)

    sorted_linked_list = merge_sort(l)
    print(sorted_linked_list)