from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h_map = {}
        more_occur = nums[0]
        for num in nums:
            if num in h_map.keys():
                h_map[num] += 1
            else:
                h_map[num] = 1
            if h_map[num] > h_map[more_occur]:
                more_occur = num
        return more_occur
