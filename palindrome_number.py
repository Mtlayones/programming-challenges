class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        array = []
        while x != 0:
            temp = x // 10
            array.append(x - (temp*10))
            x = temp
        midPoint = len(array) // 2
        for x in range(midPoint):
            if array[x] != array[-1 - x]:
                return False
        return True


if __name__ == "__main__":
    print(Solution().isPalindrome(10))
