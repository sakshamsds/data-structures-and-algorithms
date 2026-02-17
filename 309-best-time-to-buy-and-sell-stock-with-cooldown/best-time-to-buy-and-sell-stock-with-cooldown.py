class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        
        def dfs(i, prev):
            if i >= len(prices):
                return 0

            if (i, prev) in cache:
                return cache[(i, prev)]
            
            # don't buy/sell
            profit = dfs(i + 1, prev)

            # buy the stock
            profit = max(profit, dfs(i + 1, prices[i]))

            # sell the stock
            # can sell only if bought previously
            if prev >= 0:
                profit = max(profit, prices[i] - prev + dfs(i + 2, -1))

            cache[(i, prev)] = profit
            return profit

        return dfs(0, -1)