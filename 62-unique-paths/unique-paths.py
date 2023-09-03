class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [0] * (n + 1)
        dp[1] = 1

        for r in range(m):
            new_dp = [0] * (n + 1)
            for c in range(1, n + 1):
                new_dp[c] = new_dp[c - 1] + dp[c]
            dp = new_dp
            # print(dp)

        # print(dp)
        return dp[-1]
            
        