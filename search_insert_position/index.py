from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        divisor = len(nums) // 2
        index = divisor
        while divisor != 0 and index < len(nums) and index >= 0:
            if index - 1 != -1 and target >= nums[index - 1] and target <= nums[index]:
                if target == nums[index-1]:
                    index -= 1
                break
            if index + 1 != len(nums) and target > nums[index] and target <= nums[index + 1]:
                index += 1
                break
            divisor //= 2
            if target > nums[index]:
                index += divisor
            else:
                index -= divisor
        if divisor == 0:
            if target <= nums[0]:
                index = 0
            elif target == nums[-1]:
                index = len(nums) - 1
            else:
                index = len(nums)
        return index
