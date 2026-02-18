class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, can_buy):
            if i >= len(prices):
                return 0

            if (i, can_buy) in dp:
                return dp[(i, can_buy)]

            cooldown = dfs(i + 1, can_buy)
            if can_buy:
                buy = dfs(i + 1, False) - prices[i]
                profit = max(buy, cooldown)
            else:
                sell = dfs(i + 2, True) + prices[i]
                profit = max(sell, cooldown)

            dp[(i, can_buy)] = profit
            return profit

        return dfs(0, True)