from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        newArray = []
        for idx in range(n):
            newArray.extend([nums[idx], nums[idx + n]])
        return newArray
