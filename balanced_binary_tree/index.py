from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def traversal(root: Optional[TreeNode], height: int) -> int:
            if root == None:
                return height - 1
            if root.left == None and root.right == None:
                return height
            left_height = traversal(root.left, height + 1)
            right_height = traversal(root.right, height + 1)
            if min(left_height, right_height) == -1:
                return -1
            diff = abs(left_height - right_height)
            max_height = max(left_height, right_height)
            return max_height if diff <= 1 else -1
        if root == None:
            return True
        return traversal(root, 0) != -1
