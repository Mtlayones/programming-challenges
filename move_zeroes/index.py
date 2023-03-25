from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = temp = 0
        while temp < len(nums):
            if nums[left] != 0:
                left += 1
                temp += 1
                continue

            if nums[temp] != 0:
                nums[left] = nums[temp]
                nums[temp] = 0
                continue

            temp += 1
