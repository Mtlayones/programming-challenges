class Solution(object):
    def twoSum(self, nums, target):
        for itrX in range(len(nums)):
            findElement = target - nums[itrX]
            if itrX == len(nums) - 1:
                break
            for itrY in range(itrX + 1, len(nums)):
                if nums[itrY] == findElement:
                    return [itrX, itrY]
        return [0, 0]
