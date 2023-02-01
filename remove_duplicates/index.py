from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        setList = list(set(nums))
        setList.sort()
        nums[0:len(setList)] = setList
        nums[len(setList):] = ['_' for x in range(len(nums[len(setList):]))]
        return len(setList)
