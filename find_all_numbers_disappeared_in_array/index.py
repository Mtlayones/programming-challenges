from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return_list = [x for x in range(1, len(nums) + 1)]
        nums.sort()
        itr = 0
        for num in nums:
            if num > return_list[itr]:
                itr += num - return_list[itr]
            if num == return_list[itr]:
                return_list.pop(itr)
            if itr >= len(return_list):
                break
        return return_list
