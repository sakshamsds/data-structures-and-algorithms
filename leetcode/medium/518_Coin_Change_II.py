# 0/1, unbounded knapsack problem
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # TC - O(n*m)
        # SC - O(n)
        dp = [1] + [0] * amount

        for coin in coins:
            next_dp = [1] + [0] * amount
            for money in range(1, amount + 1):
                if coin > money:
                    next_dp[money] = dp[money]
                else:
                    next_dp[money] = dp[money] + next_dp[money - coin]
            dp = next_dp

        return dp[-1]

        # # memoization solution
        # cache = {}

        # def dfs(i, a):
        #     if a == amount:
        #         return 1
        #     if a > amount:
        #         return 0
        #     if i == len(coins):     # no more coins left
        #         return 0
        #     if (i, a) in cache:
        #         return cache[(i, a)]
            
        #     cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a) 
        #     return cache[(i, a)]
        
        # return dfs(0, 0)
            


        # dp = [[1] + [0] * amount for _ in range(len(coins))]
        # # for i in range(len(dp)):
        #     # dp[i][0] = 1

        # for i in range(len(coins)):
        #     for money in range(1, amount + 1):
        #         if coins[i] > money:
        #             # print(i, money, dp[i - 1][money])
        #             dp[i][money] = dp[i - 1][money]
        #         else:
        #             dp[i][money] = dp[i - 1][money] + dp[i][money - coins[i]]

        # # print(dp)
        # return dp[-1][-1]