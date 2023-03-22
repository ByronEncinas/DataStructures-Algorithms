# Theory: https://www.youtube.com/watch?v=gs2LMfuOR9k
""" 
LCA:    p = q returns root
BT:     is a validated Tree:
            such that root.left.val < root.val < root.right.val

if LCA problem implicitly says our BT is valid: Then

            10
        /        \
    8                12     
  /   \           /      \
7       9        11       13

let root = Node(10)
let p = 9, q = 8

since q,p are both < root 
then the branch which contains them is the one
with root = root.left

if q < root and p > root
then their common ancestor is root
 """

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q) -> 'TreeNode':
        """ 
        All Node.val are unique.
        p != q
        p and q will exist in the BST.
        """
        # CASES:
        # 1) q,p < root then left
        # 2) q,p > root then right
        # 3) if either q,p < root < p,q then LCA is root
        while root:
            if q.val < root.val and p.val < root.val: # 1) q,p < root then left
                root = root.left
            elif root.val < q.val and root.val < p.val: # 2) q,p > root then right
                root = root.right
            else:
                return root