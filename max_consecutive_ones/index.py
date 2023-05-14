from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        partial_count = 0
        nums.append(0)
        for num in nums:
            if num == 1:
                partial_count += 1
            if num == 0 and partial_count > count:
                count = partial_count
            if num == 0 and partial_count > 0:
                partial_count = 0
        return count
