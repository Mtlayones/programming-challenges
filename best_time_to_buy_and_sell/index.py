from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        least_price = None
        for price in prices:
            if least_price == None or price < least_price:
                least_price = price
            elif least_price < price and max_profit < price - least_price:
                max_profit = price - least_price
        return max_profit
