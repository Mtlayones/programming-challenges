from math import log, pow


class Solution:
    def isPowerOfThree(self, n: int) -> int:
        if n <= 0:
            return False
        power = round(log(n, 3))
        return 3 ** power == n
