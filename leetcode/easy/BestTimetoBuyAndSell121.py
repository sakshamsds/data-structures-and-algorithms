from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min = prices[0]
        max_profit = float("-inf")

        for price in prices:
            max_profit = max(max_profit, price - current_min)
            if price < current_min:
                current_min = price

        return max_profit