class Solution(object):
    def twoSum(self, nums, target):
        # iterating through the list of numbers
        for itrX in range(len(nums)):
            # getting the other element in list
            findElement = target - nums[itrX]
            # no found element
            if itrX == len(nums) - 1:
                break
            # checking if the other element is in sublist after the current element
            for itrY in range(itrX + 1, len(nums)):
                # if found return the indices of the two element
                if nums[itrY] == findElement:
                    return [itrX, itrY]
        return [0, 0]
