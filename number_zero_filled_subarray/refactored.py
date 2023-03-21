from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zero_occurrence = temp_zero = 0
        for num in nums:
            if num == 0:
                temp_zero += 1
                zero_occurrence += temp_zero
                continue
            temp_zero = 0
        return zero_occurrence
