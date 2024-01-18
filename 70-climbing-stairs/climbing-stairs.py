'''
dp[n] = dp[n - 1] + dp[n - 2]
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        n0, n1 = 1, 1

        for i in range(2, n + 1):
            n0, n1 = n1, n0 + n1

        return n1