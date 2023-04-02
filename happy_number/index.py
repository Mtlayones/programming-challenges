class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        hash_map = set()
        while n not in hash_map:
            hash_map.add(n)
            total_sum = 0
            while n != 0:
                total_sum = (n % 10) ** 2
                n //= 10
            if total_sum == 1:
                return True
            n = total_sum
        return False
