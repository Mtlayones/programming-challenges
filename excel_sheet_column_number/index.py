class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        h_map = {chr(64+i): i for i in range(1, 27)}
        length = len(columnTitle)
        col_num = 0
        ctr = 1
        for col_title in columnTitle:
            col_num += h_map[col_title] * (26 ** (length - ctr))
            ctr += 1
        return col_num
