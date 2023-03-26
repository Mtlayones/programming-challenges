class Solution:
    def firstUniqChar(self, s: str) -> int:
        lowercase_alpha = [0 for i in range(26)]
        left = 0
        for character in s:
            lowercase_alpha[ord(character) - 97] += 1
            while left < len(s) and lowercase_alpha[ord(s[left]) - 97] > 1:
                left += 1
        return left if left < len(s) else -1
