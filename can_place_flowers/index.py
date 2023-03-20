from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        total_flowers = 0

        for itr in range(len(flowerbed)):
            if itr == 0 and itr == len(flowerbed)-1:
                if flowerbed[itr] == 0:
                    total_flowers += 1
                continue

            if itr == 0:
                if flowerbed[itr] == 0 and flowerbed[itr + 1] == 0:
                    total_flowers += 1
                    flowerbed[itr] = 1
                continue

            if itr == len(flowerbed)-1:
                if flowerbed[itr] == 0 and flowerbed[itr - 1] == 0:
                    total_flowers += 1
                    flowerbed[itr] = 1
                continue

            if flowerbed[itr] == 0 and flowerbed[itr + 1] == 0 and flowerbed[itr - 1] == 0:
                total_flowers += 1
                flowerbed[itr] = 1

        return total_flowers >= n
