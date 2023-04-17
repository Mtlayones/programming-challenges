from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_value = max(candies)
        for itr in range(len(candies)):
            candies[itr] = candies[itr]+extraCandies >= max_value
        return candies
