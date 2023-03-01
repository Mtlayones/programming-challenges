from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        prev = None
        for num in nums:
            if prev != None and abs(prev - num) != 1:
                return num - 1
            prev = num
        return len(nums) if prev != len(nums) else 0
