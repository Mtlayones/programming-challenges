class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(list(s))
        t = sorted(list(t))
        for itr in range(len(t)):
            if itr == len(s):
                return t[itr]
            if t[itr] != s[itr]:
                return t[itr]
        return ''
