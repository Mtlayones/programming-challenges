from math import log, pow


class Solution:
    def isPowerOfFour(self, n: int) -> int:
        if n <= 0:
            return False
        power = log(n, 4)
        return power == 0 or int(power) != 0 and power / int(power) == 1
