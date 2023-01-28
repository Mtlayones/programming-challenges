class Solution(object):
    def lengthOfLongestSubstring(self, s):
        lengthSubstring = 0
        temp = []
        for character in s:
            if character in set(temp):
                lengthSubstring = len(temp) if len(
                    temp) > lengthSubstring else lengthSubstring
                index = temp.index(character)
                temp = temp[index+1:]
            temp.append(character)
        return lengthSubstring if lengthSubstring > len(temp) else len(temp)
