class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        h_map = {num: chr(64+num) for num in range(1, 27)}
        title = ''
        while columnNumber > 26:
            char_num = columnNumber // 26
            if columnNumber % 26 == 0:
                char_num -= 1
            cnt = 1
            while char_num > 26:
                cnt += 1
                char_num //= 26
            title += h_map[char_num]
            columnNumber -= char_num * (26 ** cnt)
        if columnNumber != 0:
            title += h_map[columnNumber]
        return title
