from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDepth(self, node: Optional[TreeNode]) -> int:
        if node == None:
            return 0
        return max(self.findDepth(node.left), self.findDepth(node.right)) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return 0 if root == None else self.findDepth(root)
