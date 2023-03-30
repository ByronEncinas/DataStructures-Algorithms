"""
Root = Exactly 1 Node with no parent
Leaf = Node with no children
Parent = whoever has 2 or 1 childen
Child = whoever has 1 parent
"""

"""
Binary Tree Node class
"""

class Node:
    def __init__(self, root):
        self.root = root
        self.right = None
        self.left = None

    def __repr__(self):
        return "<class 'Node Tree': %s>" % self.root

def depthFirstValues(rootNode):
    # time: O(n)
    if rootNode.root == None:
        return []
    
    stack = [rootNode]
    path = []
    graph = dict() 

    while len(stack) > 0:
        current = stack.pop() ## will be a Node
        path.append(current.root)
        graph[str(current.root)] = []

        if current.right: ## if right or left isn't None
            stack.append(current.right)
            graph[str(current.root)].append(str(current.right.root))

        if current.left:
            stack.append(current.left)
            graph[str(current.root)].append(str(current.left.root))

    return graph, path

def recursive_depthFirstValues(graph, source, path = []):
    ## graph is a dict() in the form
    """ 
    graph = {"A":["B","C", "D"],
           "B":["E"],
           "C":["F","G"],
           "D":["H"],
           "E":["I"],
           "F":["J"]}
    """
    ## Source is the keyName of the dict() where we start
    ## path is the list result of all keyNames
    if source not in path:
        path.append(source)
        if source not in graph:
            # leaf node, backtrack
            return path
        for neighbour in graph[source]:
            path = recursive_depthFirstValues(graph, neighbour, path)
    return path

def depthBreadthValues(rootNode):
    ## time & space: O(n)
    ## Queue has back and front, 
    ## they enter back and leave front
    if rootNode.root == None:
        return []

    Queue = [rootNode]
    path = []

    while len(Queue) > 0:
        current = Queue.pop(0)
        path.append(current.root)
        if current.left != None:
            Queue.append(current.left)
        if current.right != None:
            Queue.append(current.right)

    return path

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c 
b.left = d
b.right = e
c.right = f

#graph1, path1 = depthFirstValues(a)
#path2 = depthBreadthValues(a)

#print(path1) ## ['a', 'b', 'd', 'e', 'c', 'f']
#print(graph1)
#print(path2) ## ['a', 'b', 'c', 'd', 'e', 'f']
#graph = {'a': ['c', 'b'], 'b': ['e', 'd'], 'd': [], 'e': [], 'c': ['f'], 'f': []}
#x = recursive_depthFirstValues(graph, 'a')
#print(x)



""" 
           a
        /     \
      b          c
   /    \          \
 d        e          f
"""

""" 
Create:
add
remove
insert

"""

