class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}
        for itr in range(len(s)):
            if s[itr] in s_map.keys() and t[itr] in t_map.keys():
                if s_map[s[itr]] != t_map[t[itr]]:
                    return False
                s_map[s[itr]] = t_map[t[itr]] = itr
            elif s[itr] not in s_map.keys() and t[itr] not in t_map.keys():
                s_map[s[itr]] = t_map[t[itr]] = itr
            else:
                return False
        return True
