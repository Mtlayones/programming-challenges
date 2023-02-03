class Solution:
    def isValid(self, s: str) -> bool:
        parenthesisMap = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack = []
        for parenthesis in s:
            if parenthesis not in set(parenthesisMap.keys()):
                stack.append(parenthesis)
            else:
                otherParenthesis = stack.pop() if len(stack) != 0 else ""
                if parenthesisMap[parenthesis] != otherParenthesis:
                    return False
        if len(stack) != 0:
            return False
        return True
