from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum_leaf_leaves = 0

        def inorder(root: Optional[TreeNode]) -> int:
            if root == None:
                return 0
            if root.left == None and root.right == None:
                return root.val
            left = inorder(root.left)
            right = inorder(root.right)
            return 0

        inorder(root)

        return self.sum_leaf_leaves
