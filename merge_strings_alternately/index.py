class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string = ''
        minLength = min(len(word1), len(word2))
        for i in range(minLength):
            string += word1[i] + word2[i]
        return string + (word1[minLength:] if len(word1) != minLength else word2[minLength:])
