'''
        1   2   3   4   5   6   7   8   9   10  11
        1   1   2   2   1   2   2   3   3   2   3
'''

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        for a in range(1, amount + 1):
            for coin in coins:
                if (a - coin) >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])
            # print(dp)
        return dp[-1] if dp[-1] != float('inf') else -1
