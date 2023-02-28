class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        listS = sorted(list(s))
        listT = sorted(list(t))
        for itr in range(len(listS)):
            if listS[itr] != listT[itr]:
                return False
        return True
