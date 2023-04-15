from math import log2, pow


class Solution:
    def hammingWeight(self, n: int) -> int:
        num_1bits = 0
        if n % 2 == 1:
            num_1bits += 1
            n -= 1
        while n != 0:
            n -= pow(2, int(log2(n)))
            num_1bits += 1
        return num_1bits
