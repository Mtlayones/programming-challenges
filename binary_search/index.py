from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while (right - left) != 0:
            mid_point = left + (right - left) // 2
            if nums[mid_point] == target:
                return mid_point
            elif target > nums[mid_point]:
                left = mid_point + 1
            else:
                right = mid_point
        return -1
