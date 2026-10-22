class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for _ in range(1, m):
            new_dp = [1] * n
            for c in range(1, n):
                new_dp[c] = dp[c] + new_dp[c - 1]
            dp = new_dp

        return dp[-1]