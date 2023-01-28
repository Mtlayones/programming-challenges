class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lengthOfString = len(s)
        lengthOfSubstring = 0
        # used for storing the index of the characters and character checking
        hashMap = {}
        # used for storing the index of the first character of the substring
        slidingI = 0
        # sliding through the string
        for slidingJ in range(lengthOfString):
            # if the current character is already been seen
            if s[slidingJ] in hashMap:
                # checking if the found character is in the current substring or in the previous substring
                slidingI = max(hashMap[s[slidingJ]], slidingI)
            # checking if the current substring is larger the previous substring
            lengthOfSubstring = max(lengthOfSubstring, slidingJ - slidingI + 1)
            # updating the current index of the characters in the hashmap
            hashMap[s[slidingJ]] = slidingJ + 1
        return lengthOfSubstring
