from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        newList = []
        start = prev = nums[0]
        for itr in range(1, len(nums)):
            if abs(nums[itr] - prev) != 1:
                newList.append("{}->{}".format(start, prev)
                               if start != prev else str(start))
                start = nums[itr]
            prev = nums[itr]
        newList.append("{}->{}".format(start, prev)
                       if start != prev else str(start))
        return newList
