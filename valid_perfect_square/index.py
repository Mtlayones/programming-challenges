class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        # using binary search
        left = 1
        right = num
        while right - left >= 0:
            mid_point = (right + left) // 2
            if mid_point * mid_point == num:
                return True
            elif mid_point * mid_point > num:
                right = mid_point - 1
            else:
                left = mid_point + 1
        return False
