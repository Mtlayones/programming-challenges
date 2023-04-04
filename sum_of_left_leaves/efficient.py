from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def traversal(root: Optional[TreeNode], is_left: bool) -> int:
            if root == None:
                return 0
            if root.left == None and root.right == None and is_left:
                return root.val
            left = traversal(root.left, True)
            right = traversal(root.right, False)
            return left + right
        return traversal(root, False)
