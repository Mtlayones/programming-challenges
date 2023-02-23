from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmap = dict()
        for idx in range(len(nums)):
            if nums[idx] in hmap.keys() and abs(idx - hmap[nums[idx]]) <= k:
                return True
            hmap[nums[idx]] = idx
        return False
