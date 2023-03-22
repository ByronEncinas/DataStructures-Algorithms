# Definition for a binary tree Node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        levelstack = list()
        self.depth_first(root,0,levelstack) 
        return levelstack

    def depth_first(self, root, depth, levelstack):
        if root: #we only care if there is a root
            if depth>=len(levelstack): # if its our first time in this depth
                levelstack.append([])  # add space if needed
            levelstack[depth].append(root.val) 
            self.depth_first(root.left,depth+1,levelstack) 
            self.depth_first(root.right,depth+1,levelstack) 


## Best RunTime
from collections import deque
class Solution2:
    def levelOrder(self, root):
        stack = deque([root])
        result = []
        while stack:
            s = len(stack)
            temp = []
            for _ in range(s):
                if node := stack.popleft():
                    temp.append(node.val)
                    stack.append(node.left)
                    stack.append(node.right)
            if temp:
                result.append(temp)
        return result