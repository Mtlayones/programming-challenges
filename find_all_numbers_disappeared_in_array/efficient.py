from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)
        return_list = []
        for itr in range(1, len(nums) + 1):
            if itr not in set_nums:
                return_list.append(itr)
        return return_list
