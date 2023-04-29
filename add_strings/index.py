class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        right_1 = len(num1) - 1
        right_2 = len(num2) - 1
        carry = 0
        string_sum = ''
        while right_1 >= 0 and right_2 >= 0:
            num_1 = ord(num1[right_1]) - 48
            num_2 = ord(num2[right_2]) - 48
            total = num_1 + num_2 + carry
            carry = total // 10
            string_sum = chr(48 + (total % 10)) + string_sum
            right_1 -= 1
            right_2 -= 1
        new_string = num1[:right_1 + 1] + num2[:right_2 + 1]
        if carry != 0:
            right = len(new_string) - 1
            while carry != 0 and right >= 0:
                total = ord(new_string[right]) - 48 + carry
                carry = total // 10
                string_sum = chr(48 + (total % 10)) + string_sum
                right -= 1
            if carry != 0:
                string_sum = chr(48+carry) + string_sum
            string_sum = new_string[:right+1] + string_sum
        elif not (right_1 < 0 and right_2 < 0):
            string_sum = new_string + string_sum

        return string_sum
