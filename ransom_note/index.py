class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        alphabet = [0 for i in range(26)]
        for character in magazine:
            alphabet[ord(character)] += 1

        for character in ransomNote:
            if alphabet[ord(character)] > 0:
                alphabet[ord(character)] -= 1
            else:
                return False
        return True
