from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while len(nums2) != 0:
            num = nums2.pop(0)
            start = 0
            end = m - 1
            ans = 0
            while start <= end:
                mid = (start + end) // 2
                if nums1[mid] < num:
                    start = ans = mid + 1
                elif nums1[mid] > num:
                    end = mid - 1
                else:
                    ans = mid
                    break
            nums1.pop()
            nums1.insert(ans, num)
            m += 1
