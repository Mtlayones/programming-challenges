class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}
        left = 0
        right = len(s) - 1
        list_string = list(s)
        while left < right:
            if list_string[left] in VOWELS and list_string[right] in VOWELS:
                temp = list_string[left]
                list_string[left] = list_string[right]
                list_string[right] = temp
                left += 1
                right -= 1
                continue
            if list_string[left] not in VOWELS:
                left += 1
            if list_string[right] not in VOWELS:
                right -= 1
        return ''.join(list_string)
