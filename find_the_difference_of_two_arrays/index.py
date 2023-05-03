from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums_set1 = set(nums1)
        nums_set2 = set(nums2)
        return [list(nums_set1.difference(nums_set2)), list(nums_set2.difference(nums_set1))]
