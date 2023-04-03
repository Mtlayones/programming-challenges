from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        num_boats = 0
        left = 0
        right = len(people) - 1
        people.sort()
        while left <= right:
            if people[right] + people[left] <= limit:
                left += 1
            right -= 1
            num_boats += 1
        return num_boats
