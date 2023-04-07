class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ''
        digit = 0
        roman_representation = "IVXLCDM"
        while num != 0:
            current_digit = num % 10
            if current_digit < 4:
                roman = current_digit * roman_representation[digit] + roman
            elif current_digit < 5:
                roman = roman_representation[digit] + \
                    roman_representation[digit + 1] + roman
            elif current_digit < 9:
                roman = roman_representation[digit + 1] + \
                    (roman_representation[digit] * (current_digit - 5)) + roman
            else:
                roman = roman_representation[digit] + \
                    roman_representation[digit + 2] + roman
            num //= 10
            digit += 2

        return roman
