from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def createBST(nums: List[int], left: int, right: int) -> Optional[TreeNode]:
            if right-left <= 0:
                return None
            mid = (right + left) // 2
            node = TreeNode(val=nums[mid])
            if right-left == 1:
                return node
            node.left = createBST(nums, left, mid)
            node.right = createBST(nums, mid + 1, right)
            return node
        return createBST(nums, 0, len(nums))
