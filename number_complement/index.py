from math import floor, log2


class Solution:
    def findComplement(self, num: int) -> int:
        if num == 1:
            return 0
        if num == 0:
            return 1
        max_num = pow(2, floor(log2(num)) + 1) - 1
        return num ^ max_num
