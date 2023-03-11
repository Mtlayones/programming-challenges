from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        new_list1 = [1]
        new_list2 = [1]
        # using binomial coefficient
        for itr in range(0, rowIndex//2):
            element = new_list1[itr] * (rowIndex - itr) // (itr + 1)
            new_list1.append(element)
            if itr + 1 == rowIndex - (itr + 1):
                continue
            new_list2.insert(0, element)
        return new_list1 + new_list2
