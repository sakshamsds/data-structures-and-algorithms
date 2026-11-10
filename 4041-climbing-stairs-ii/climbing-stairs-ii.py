'''
    dp[n] = cost[n] + min(
        dp[n - 1] + 1,
        dp[n - 2] + 4,
        dp[n - 3] + 9
    )
'''


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        a, b, c = 0, 0, 0
        for i in range(n):
            a, b, c = b, c, min(a + 9, b + 4, c + 1) + costs[i]
        return c