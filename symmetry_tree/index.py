from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkSymmetry(self, left: Optional[TreeNode], right: Optional[TreeNode]):
        if left == None and right == None:
            return True
        if left != None and right != None and left.val == right.val:
            return self.checkSymmetry(left.left, right.right) and self.checkSymmetry(left.right, right.left)
        return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        return self.checkSymmetry(root.left, root.right)
