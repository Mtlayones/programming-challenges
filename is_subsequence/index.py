class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        left_s = 0
        left_t = 0
        while left_t < len(t):
            if s[left_s] == t[left_t]:
                left_s += 1
            if left_s == len(s):
                return True
            left_t += 1
        return False
