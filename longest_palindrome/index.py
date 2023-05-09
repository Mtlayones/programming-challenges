class Solution:
    def longestPalindrome(self, s: str) -> int:
        h_map = {}
        for character in s:
            if character not in h_map.keys():
                h_map[character] = 1
                continue
            h_map[character] += 1
        extra = 0
        total = 0
        for key in h_map.keys():
            if h_map[key] % 2 == 1:
                if extra == 0:
                    extra = 1
                total -= 1
            total += h_map[key]
        return total + extra
