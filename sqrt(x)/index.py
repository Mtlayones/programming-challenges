class Solution:
    def mySqrt(self, x: int) -> int:
        output = x
        for i in range(1, (x//2)+1):
            if i * i > x:
                return output
            output = i
        return output
