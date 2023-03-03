class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack) or needle not in haystack:
            return -1
        if len(needle) == len(haystack) and needle == haystack:
            return 0
        lengthNeedle = len(needle)
        for itr in range(len(haystack)):
            if itr + lengthNeedle > len(haystack):
                return -1
            if haystack[itr:itr+lengthNeedle] == needle:
                return itr
