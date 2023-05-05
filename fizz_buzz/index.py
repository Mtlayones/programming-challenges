from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        list_1 = []
        for i in range(n):
            if (i+1) % 15 == 0:
                list_1.append("FizzBuzz")
            elif (i+1) % 5 == 0:
                list_1.append("Buzz")
            elif (i+1) % 3 == 0:
                list_1.append("Fizz")
            else:
                list_1.append(f"{i+1}")
        return list_1
