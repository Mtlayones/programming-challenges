class Solution:
    def addBinary(self, a: str, b: str) -> str:
        newA = list(a)
        newB = list(b)
        newBinary = []
        carry = 0
        while len(newA) != 0 and len(newB) != 0:
            temp = int(newA.pop()) + int(newB.pop())
            if temp not in {0, 1}:
                newBinary.insert(0, str(carry))
                carry = 1
            else:
                newBinary.insert(0, str(temp ^ carry))
                carry = temp & carry
        while carry != 0:
            if len(newA) != 0:
                temp = int(newA.pop())
            elif len(newB) != 0:
                temp = int(newB.pop())
            else:
                newBinary.insert(0, str(carry))
                break
            newBinary.insert(0, str(temp ^ carry))
            carry = temp & carry
        if len(newA) != 0:
            newBinary = newA + newBinary
        else:
            newBinary = newB + newBinary
        return ''.join(newBinary)
