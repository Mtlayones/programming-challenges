from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self._myList = nums

    def sumRange(self, left: int, right: int) -> int:
        sum_range = 0
        for i in range(left, right + 1):
            sum_range += self._myList[i]
        return sum_range
