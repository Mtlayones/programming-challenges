from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        ans = 0
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = ans = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid
        return ans
