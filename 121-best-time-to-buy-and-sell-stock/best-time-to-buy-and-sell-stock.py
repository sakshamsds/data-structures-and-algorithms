class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        mx_profit = 0
        for price in prices:
            buy_price = min(buy_price, price)
            mx_profit = max(mx_profit, price - buy_price)
        return mx_profit