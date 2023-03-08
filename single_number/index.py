from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_map = {}
        for num in nums:
            if num not in hash_map.keys():
                hash_map[num] = 1
                continue
            hash_map[num] += 1
        return sorted(hash_map.items(), key=lambda x: x[1]).pop(0)[0]
