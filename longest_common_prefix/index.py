from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        container = []
        currentIndex = 0
        for string in strs:
            index = 0
            tempContainer = []
            for character in string:
                if (index < len(container) and container[index] != character) or (currentIndex != 0 and index >= len(container)):
                    break
                else:
                    tempContainer.append(character)
                index += 1
            container = tempContainer
            if len(container) == 0:
                break
            currentIndex += 1
        return ''.join(container)
