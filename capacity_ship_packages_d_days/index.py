from typing import List


class Solution:
    def findMinimalDays(self, maximumCapacity: int, weights: List[int]) -> int:
        capacity = 0
        days = 1
        for weight in weights:
            if weight + capacity > maximumCapacity:
                capacity = weight
                days += 1
                continue
            capacity += weight
        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        right = sum(weights)
        left = max(weights)

        while left < right:
            midPoint = (left + right) // 2
            if self.findMinimalDays(midPoint, weights) <= days:
                right = midPoint
                continue
            left = midPoint + 1
        return left
