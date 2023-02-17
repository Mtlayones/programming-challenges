from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.minDiff = float('inf')
        self.predecessorVal = None
        self.inOrderTraversal(root)
        return self.minDiff

    def inOrderTraversal(self, root: TreeNode) -> None:
        if root == None:
            return
        self.inOrderTraversal(root.left)
        if self.predecessorVal != None:
            self.minDiff = min(self.minDiff, root.val - self.predecessorVal)
        self.predecessorVal = root.val
        self.inOrderTraversal(root.right)
