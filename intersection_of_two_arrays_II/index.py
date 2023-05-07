from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h = {}
        if (len(nums1) >= len(nums2)):
            max_nums = nums1
            min_nums = nums2
        else:
            max_nums = nums2
            min_nums = nums1
        for num in max_nums:
            if num in h.keys():
                h[num] += 1
                continue
            h[num] = 1
        min_nums.sort()
        ans_list = []
        for num in min_nums:
            if num in h.keys():
                if h[num] == 0:
                    continue
                ans_list.append(num)
                h[num] -= 1

        return ans_list
