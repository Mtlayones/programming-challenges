from typing import List


class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        hset = set()
        for idx in nums:
            if idx in hset:
                return True
            else:
                hset.add(idx)
