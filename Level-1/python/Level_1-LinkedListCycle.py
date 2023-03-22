# hash table - linked list
# best TIME
class Solution1(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        hashTable = set()
        current = head
        while current:
            if current in hashTable:
                return current
            hashTable.add(current)
            current = current.next
        return current

## best MEMORY
class Solution2(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        while fast and fast.next:
            print(slow.val, fast.val)
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        else:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow