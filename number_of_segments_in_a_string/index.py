class Solution:
    def countSegments(self, s: str) -> int:
        prev = False
        count = 0
        for character in s:
            if not prev and character != " ":
                count += 1
                prev = True
            elif prev and character == " ":
                prev = False
        return count
