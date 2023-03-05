from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.inorder(root, targetSum, 0)

    def inorder(self, root: Optional[TreeNode], targetSum: int, findSum: int) -> bool:
        if root == None:
            return False
        if (findSum + root.val) == targetSum and root.left == None and root.right == None:
            return True
        if self.inorder(root.left, targetSum, findSum + root.val):
            return True
        return self.inorder(root.right, targetSum, findSum + root.val)
