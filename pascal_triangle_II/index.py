from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal_triangle = [[1]]
        for itrX in range(2, rowIndex+2):
            pascal_triangle.append([])
            for itrY in range(itrX):
                if itrY == 0 or itrY == itrX - 1:
                    pascal_triangle[itrX-1].append(1)
                else:
                    pascal_triangle[itrX-1].append(
                        pascal_triangle[itrX-2][itrY-1] + pascal_triangle[itrX-2][itrY])
        return pascal_triangle.pop()
