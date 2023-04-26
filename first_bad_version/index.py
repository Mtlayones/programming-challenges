class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while right - left != 0:
            mid_point = left + (right - left) // 2
            if isBadVersion(mid_point):
                right = mid_point
            else:
                left = mid_point + 1
        return left
