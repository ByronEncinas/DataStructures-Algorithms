class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


## My Solution
## Python3
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stack = [] ## setup solution variable
        self.recursive_method(root, stack) ## use class private function
        return stack # return updated variable

    def recursive_method(self, root, stack):
        if root is None: ## each leaf will come to this
            return 
        ## each iteration we save up the root.val
        stack.append(root.val)
        for child in root.children:
            ## no need to return, just update stack list
            self.recursive_method(child, stack)

## Python
class Solution:
    def preorder(self, root):
        
        stack = []
        self.recursive_method(root, stack)
        return stack

    def recursive_method(self, root, stack):
        if root is None:
            return 
        stack.append(root.val)
        ## each iteration we save up the root.val
        for child in root.children:
            self.recursive_method(child, stack)