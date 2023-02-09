class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        low = 1
        high = x
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            if x//mid == mid:
                return mid
            elif x//mid < mid:
                high = mid - 1
            else:
                low = mid + 1
                ans = mid
        return ans
