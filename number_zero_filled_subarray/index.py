from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zero_occurrence = temp_zero = 0
        for num in nums:
            if num == 0:
                temp_zero += 1
            elif temp_zero != 0:
                zero_occurence += (temp_zero/2)*(temp_zero+1)
                temp_zero = 0
        if temp_zero != 0:
            zero_occurence += (temp_zero/2)*(temp_zero+1)
        return int(zero_occurrence)
