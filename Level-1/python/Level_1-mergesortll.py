class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# iteratively
def mergeTwoLists1(self, l1, l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next
    
# recursively    
def mergeTwoLists2(self, l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2
        
# in-place, iteratively        
def mergeTwoLists(self, l1, l2):
    if None in (l1, l2):
        return l1 or l2
    dummy = cur = ListNode(0)
    dummy.next = l1
    while l1 and l2:
        if l1.val < l2.val:
            l1 = l1.next
        else:
            nxt = cur.next
            cur.next = l2
            tmp = l2.next
            l2.next = nxt
            l2 = tmp
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

    ## My attempt


class Solution(object):
    def mergeTwoLists_(self, list1, list2):
        sorted_merged = ListNode(0) 
        dummy = sorted_merged
        # dummy point to the beggining of sorted_merged
        # whenever both lists are not empty/None

        while list1 != None and list2 != None:
            # we sort heads
            if list1.val < list2.val: 
                # sort heads and dummy is absorbing 
                # from sorted_merged each iterations
                sorted_merged.next = list1
                list1 = list1.next                
            else: 
                sorted_merged.next = list2
                list2 = list2.next
            # we move our sorted_merged.next to sorted_merged
            # just move .next to the head
            sorted_merged = sorted_merged.next
        # if while statement is false from the beginning
        sorted_merged.next = list1 or list2  #this if any is empty return other
        return dummy.next 

    ## Best Solution In LeetCode

class Solution(object):
    def _mergeTwoLists(self, list1, list2):
        return _merge_two_sorted_list(list1, list2)

def _merge_two_sorted_list(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    if list1.val <= list2.val:
        return ListNode(val=list1.val, next=_merge_two_sorted_list(list1.next, list2))
    else:
        return ListNode(val=list2.val, next=_merge_two_sorted_list(list1, list2.next))

