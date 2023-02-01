class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x *= sign
        revertedNumber = 0
        while x != 0:
            temp = x // 10
            # temp = x // 10 and x - (temp*10) can be x%10 and x//=10
            revertedNumber = (revertedNumber * 10) + (x - (temp*10))
            x = temp
        revertedNumber *= sign
        return revertedNumber if revertedNumber >= -(2 ** 31) and revertedNumber <= (2 ** 31) - 1 else 0
