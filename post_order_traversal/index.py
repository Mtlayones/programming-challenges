from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.newList = []
        self.postorder(root)
        return self.newList

    def postorder(self, root: Optional[TreeNode]) -> None:
        if root == None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        self.newList.append(root.val)
