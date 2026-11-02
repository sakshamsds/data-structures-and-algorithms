'''
        0   1   2   3   4   5
    0   1   0   0   0   0   0
    1   1   1   1   1   1   1
    2   1   1   2   2   3   3
    5   1   1   2   2   3   4
'''

class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        # dp[coin][amt] = dp[coin - 1][amt] + dp[coin][amt - coinValue]
        dp = [1] + [0] * amount
        for coin in coins:
            for amt in range(coin, amount + 1):
                dp[amt] += dp[amt - coin]
        return dp[-1]