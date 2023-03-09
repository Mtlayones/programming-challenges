from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        bitList = [0]
        for itr in range(1, n + 1):
            bitList.append(bitList[itr//2] + (itr % 2))
        return bitList
