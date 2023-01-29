class Solution:
    def romanToInt(self, s: str) -> int:
        equivalence = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        equivalentInteger = 0
        prevValue = 0
        for roman in s:
            equivalentInteger = equivalentInteger + equivalence[roman] if equivalence[
                roman] <= prevValue else equivalentInteger - prevValue * 2 + equivalence[roman]
            prevValue = equivalence[roman]
        return equivalentInteger
