from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.current_num = 0
        self.inorder(root, 0)
        return self.current_num

    def inorder(self, root: Optional[TreeNode], current_val: int) -> None:
        if root == None:
            return
        current_val = current_val * 10 + root.val
        if root.left == None and root.right == None:
            self.current_num += current_val
        self.inorder(root.left, current_val)
        self.inorder(root.right, current_val)
