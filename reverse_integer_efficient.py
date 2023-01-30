class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = (2 ** 31) - 1
        INT_MIN = -(2 ** 31)
        revertedNumber = 0
        while x != 0:
            pop = x % 10
            x //= 10
            if revertedNumber > INT_MAX//10 or (revertedNumber == INT_MAX//10 and pop > 7):
                return 0
            if revertedNumber < INT_MIN//10 or (revertedNumber == INT_MIN//10 and pop < -8):
                return 0
            revertedNumber = revertedNumber * 10 + pop
        return revertedNumber
