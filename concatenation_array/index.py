from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newArray = []
        newArray.extend(nums)
        newArray.extend(nums)
        return newArray
