class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        cooldown = 1
        cache = {}

        def dfs(i, canBuy):
            if i >= len(prices):
                return 0
                
            if (i, canBuy) in cache:
                return cache[(i, canBuy)]
            
            # do nothing
            profit = dfs(i + 1, canBuy)

            if canBuy:  # buy
                profit = max(profit, dfs(i + 1, False) - prices[i])
            else:       # sell
                profit = max(profit, dfs(i + 1 + cooldown, True) + prices[i])

            cache[(i, canBuy)] = profit
            return profit

        return dfs(0, True)
