from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not (p != None and q != None)) or (p.val != q.val):
            if p == None and q == None:
                return True
            return False
        val = self.isSameTree(p.left, q.left)
        if not val:
            return val
        return self.isSameTree(p.right, q.right)
