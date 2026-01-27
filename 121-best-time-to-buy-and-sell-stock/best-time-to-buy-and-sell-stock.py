class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_cur = float(inf)
        max_profit = 0
        for price in prices:
            max_profit = max(max_profit, price - min_cur)
            min_cur = min(min_cur, price)

        return max_profit