class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # buy, sell, do nothing
        dp = {}

        def dfs(i, can_buy):
            if i == len(prices):
                return 0

            if (i, can_buy) in dp:
                return dp[(i, can_buy)]

            nothing = dfs(i + 1, can_buy)
            if can_buy:
                buy = dfs(i + 1, False) - prices[i]
                profit = max(buy, nothing)
            else:
                sell = dfs(i + 1, True) + prices[i] - fee
                profit = max(sell, nothing)

            dp[(i, can_buy)] = profit
            return profit

        return dfs(0, True)