from math import floor


class Solution:
    def arrangeCoins(self, n: int) -> int:
        # using quadratic equation
        factor = (-1+(1+4*n*2)**(1/2)) / 2
        return floor(factor)
