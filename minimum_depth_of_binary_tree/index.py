from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.minimum_depth = None
        self.traversal(root, 1)
        return self.minimum_depth if self.minimum_depth else 0

    def traversal(self, root: Optional[TreeNode], depth: int) -> None:
        if root == None:
            return

        if root.left == None and root.right == None:
            if self.minimum_depth:
                self.minimum_depth = min(self.minimum_depth, depth)
            else:
                self.minimum_depth = depth

        self.traversal(root.left, depth + 1)
        self.traversal(root.right, depth + 1)
