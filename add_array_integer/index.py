from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        right = len(num) - 1
        carry = 0
        while k > 0 and right > -1:
            digit = carry + num[right] + (k % 10)
            carry = digit // 10
            num[right] = digit % 10
            k //= 10
            right -= 1
        while k > 0:
            digit = carry + (k % 10)
            carry = digit // 10
            num.insert(0, digit % 10)
            k //= 10
        while right > -1 and carry == 1:
            digit = carry + num[right]
            carry = digit // 10
            num[right] = digit % 10
            right -= 1
        if carry == 1:
            num.insert(0, carry)

        return num
