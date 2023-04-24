from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort(reverse=True)
            stone = stones.pop(0) - stones.pop(0)
            if stone > 0:
                stones.append(stone)
        return 0 if len(stones) == 0 else stones[0]
