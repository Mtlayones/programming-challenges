class Solution:
    def hammingWeight(self, n: int) -> int:
        num_1bits = 0
        while n != 0:
            if n % 2 == 1:
                num_1bits += 1
            n >>= 1
        return num_1bits
