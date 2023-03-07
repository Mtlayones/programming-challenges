from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.newList = []
        self.preorder(root)
        return self.newList

    def preorder(self, root: Optional[TreeNode]) -> None:
        if root == None:
            return
        self.newList.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
