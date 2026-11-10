'''
    dp[n] = cost[n] + min(
        dp[n - 1] + 1,
        dp[n - 2] + 4,
        dp[n - 3] + 9
    )
'''


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0] + [cost for cost in costs]

        for i in range(1, n + 1):
            prev = dp[i - 1] + 1
            prev_prev = dp[i - 2] + 4 if i >= 2 else float('inf')
            prev_prev_prev = dp[i - 3] + 9 if i >= 3 else float('inf')
            dp[i] += min(prev, prev_prev, prev_prev_prev)

        return dp[-1]