from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        rightIndex = len(nums)
        leftIndex = 0
        while leftIndex < rightIndex:
            if nums[leftIndex] == val:
                rightIndex -= 1
                if nums[rightIndex] != val:
                    nums[leftIndex] = nums[rightIndex]
                else:
                    continue
            leftIndex += 1
        return rightIndex
