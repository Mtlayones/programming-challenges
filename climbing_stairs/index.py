class Solution:
    def climbStairs(self, n: int) -> int:
        # iterative version of the fibonacci algorithm
        a, b = 1, 1
        for i in range(n):
            a, b = b, a+b
        return a
