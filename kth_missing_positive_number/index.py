from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        itr = 0
        missing_num = 0
        arr_index = 0
        while itr < k:
            missing_num += 1
            while len(arr) != arr_index and missing_num == arr[arr_index]:
                missing_num = arr[arr_index] + 1
                arr_index += 1
            itr += 1
        return missing_num
