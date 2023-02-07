from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        index = -1
        while True:
            num = digits[index] + carry
            carry = num // 10
            digits[index] = num % 10
            index -= 1
            if len(digits) + index < 0 or carry == 0:
                break
        if carry != 0:
            digits.insert(0, carry)
        return digits
