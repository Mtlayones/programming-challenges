from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n <= 0:
            return True
        prev = itr = 0
        while len(flowerbed) > itr:
            if itr != len(flowerbed) - 1:
                itr += 1
            if flowerbed[itr - 1] == 0 and prev == 0 and flowerbed[itr] == 0:
                n -= 1
            elif flowerbed[itr] == 1 and itr + 1 < len(flowerbed):
                itr += 1
            prev = flowerbed[itr]
            if n <= 0:
                return True
            itr += 1
        return False
