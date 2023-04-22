class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0
        right = n
        r_guess = 1
        while True:
            mid_point = left + (right - left) // 2
            r_guess = guess(mid_point + 1)
            if r_guess == 0:
                return mid_point + 1
            elif r_guess == 1:
                left = mid_point + 1
            else:
                right = mid_point
