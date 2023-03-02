from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.newList = []
        self.inorder(root)
        return self.newList

    def inorder(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return
        self.inorder(root.left)
        self.newList.append(root.val)
        self.inorder(root.right)
