class Solution:
    def reverseBits(self, n: int) -> int:
        MAX_LENGTH = 32
        current_length = 0
        reverse_num = 0
        while n != 0:
            reverse_num = (reverse_num * 2) + (n & 1)
            n >>= 1
            current_length += 1
        if current_length != MAX_LENGTH:
            reverse_num = reverse_num * (2 ** (MAX_LENGTH - current_length))
        return reverse_num
