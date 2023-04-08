from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        num_perimeter = 0
        row_len = len(grid[0])
        col_len = len(grid)
        for col in range(col_len):
            for row in range(row_len):
                if grid[col][row] == 1:
                    num_perimeter += 4
                    if col != 0 and grid[col-1][row] == 1:
                        num_perimeter -= 1
                    if row != 0 and grid[col][row-1] == 1:
                        num_perimeter -= 1
                    if row != row_len-1 and grid[col][row+1] == 1:
                        num_perimeter -= 1
                    if col != col_len-1 and grid[col+1][row] == 1:
                        num_perimeter -= 1

        return num_perimeter
