'''
        0   1   2   3   4
    4   1   0   0   0   1
    1   1   1   1   1   2
    2   1   1   2   2   4
'''

class Solution:
    def numberOfWays(self, n: int) -> int:
        dp = [1] + [0] * n
        MOD = 10**9 + 7
        print(MOD)
        if n >= 8:
            dp[8] = 1
        if n >= 4:
            dp[4] = 1        
        
        for coin in [1, 2, 6]:
            for amt in range(coin, n + 1):
                dp[amt] = (dp[amt] + dp[amt - coin]) % MOD
        return dp[-1]