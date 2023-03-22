#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ## we set a pointer to head
        ## this code basicly is changing pointer 180°
        ## in the beginning Head: [head.val] --> [head.next]
        ## but in the code reversedHead: [head.val] <-- [head.next]
        current = head
        while current and current.next: 
            ## if current is None 
            ## or current.next is None
            ## current will travel to the list just once then it'll all stop
            next = current.next ## we set 2 as root of next = [2,3,4,5]
            current.next = next.next # current = [3,4,5]
            next.next = head # next.next = [2, head] = [2,1,3,4,5] since 1 points to 3 now 
            head = next # head = [2,1,3,4,5]
            # repeat with head = [2,1,3,4,5]
        return head
        
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 0 ## .val will have index 0
        current = head
        while (current.next):
            # count number of nodes
            current = current.next
            count += 1
        numbNodes = count-1
        for i in range(numbNodes//2 + 1):
            nextNode = head.next
            head = nextNode
        return head
""" 
current = head = [1,2,3,4,5] -> None
    first traverse:
        head = [2,1,3,4,5] -> None
    second traverse:
        head = [3,2,1,4,5] -> None
    third traverse:
        head = [4,3,2,1,5] -> None
    fourth traverse:
        head = [5,4,3,2,1] -> None
each passing it keeps moving head.val to the last position
"""


## BEST TIME SOLUTION

class Solution1(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #return head
        if(head is None): #empty linked list
            return
    
        cur=head
        while(cur.next):
            node=cur.next  
            cur.next=cur.next.next #point to the one after the next
            node.next=head
            head=node
        return head
        
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

## BEST SPACE SOLUTION

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        t = None
        c = head
        p = None
        while c:
            t = c.next
            c.next = p
            p = c
            c = t
        return p
    
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
