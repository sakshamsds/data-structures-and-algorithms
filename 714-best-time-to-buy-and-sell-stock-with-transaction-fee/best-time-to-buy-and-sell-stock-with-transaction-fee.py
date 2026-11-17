class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cache = {}

        def dfs(i, canBuy):
            if i >= len(prices):
                return 0

            if (i, canBuy) in cache:
                return cache[(i, canBuy)]
            
            profit = dfs(i + 1, canBuy)
            if canBuy:
                profit = max(profit, dfs(i + 1, False) - prices[i])
            else:
                profit = max(profit, dfs(i + 1, True) + prices[i] - fee)

            cache[(i, canBuy)] = profit
            return profit

        return dfs(0, True)