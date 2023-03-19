class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        h_map = {}
        new_list = s.split(" ")
        pattern_length = len(pattern)
        if len(new_list) != pattern_length:
            return False
        for itr in range(pattern_length):
            if pattern[itr] in h_map.keys() and h_map[pattern[itr]] != new_list[itr]:
                return False
            if pattern[itr] not in h_map.keys():
                if new_list[itr] in h_map.values():
                    return False
                h_map[pattern[itr]] = new_list[itr]
        return True
