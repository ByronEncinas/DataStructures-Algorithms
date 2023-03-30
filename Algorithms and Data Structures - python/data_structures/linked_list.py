class Node:
    ## It stores the variable and space for its content
    data = None
    next_node = None
    ## A node is an instance of a linked list, it
    ## stores info on Node content and neighboring nodes
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<class 'Node': %s>" % self.data
        
class LinkedList:
    """ 
    Singly linked list
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0 
        ## Returns number of nodes in
        ## O(n)
        while current != None:
            count += 1
            current = current.next_node
        return count
    
    def add(self, data):
        ## O(1) operation: reassigning new_node as self.head
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self,key):
        ## Search firts node cotaintin data matching key
        ## return None if not found
        ## O(n)        
        current = self.head
        while current != None:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def remove(self, key):
        ## removes data matching key O(n)
        ## if key not in linkedlist return None

        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current 
                current = current.next_node
        return current

    def insert(self, data, index):
        ## Insert new node at index position
        ## insertion O(1), but finding node O(n) times

        ## overall O(n)
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)
            
            position = index
            current = self.head

            while position > 1:
                current = new.next_node
                position -= 1
            
            prev_node = current 
            next_node = current.next_node

            return current

    def node_at_index(self,index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0
            
            while position < index:
                current = current.next_node
                position += 1
                
            return current


    def __repr__(self):
        ## prepend
        nodes = []
        current = self.head

        while current != None: ## we are not in tail
            if current is self.head:
                nodes.append("[head: %s]" %current.data)
            elif current.next_node is None:
                nodes.append("[tail: %s]" % current.data)
            else:
                nodes.append("[%s ]" % current.data)

            current = current.next_node

        return ' ->'.join(nodes)


""" 
PS D:\Algorithms and Data Structures - python> python -i .\linked_list.py
>>> N1 = Node(10)
>>> N1
<class 'Node': 10>
>>> N2 = Node(11)
>>> N1.next_node = N2
>>> N1.next_node
<class 'Node': 11> 
>>> l = LinkedList()
>>> l.add(1)
>>> l.search(1)
>>> l
"""