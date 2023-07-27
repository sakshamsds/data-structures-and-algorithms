from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)

        # bottom up dp
        for money in range(1, amount + 1):
            dp[money] = 10^4 + 1
            for coin in coins:
                if money >= coin:
                    num_coins = 1 + dp[money - coin]
                    dp[money] = min(dp[money], num_coins)

        print(dp)
        return -1 if dp[-1] == 0 else dp[-1]
        # return dp[-1]


# Solution().coinChange([1, 2, 5], 11)
Solution().coinChange([2], 3)
print(10 ** 4 + 1)