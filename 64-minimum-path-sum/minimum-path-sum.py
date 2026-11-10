class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [float('inf')] * cols
        dp[0] = 0
        for r in range(rows):
            dp[0] += grid[r][0]
            for c in range(1, cols):
                dp[c] = min(dp[c], dp[c - 1]) + grid[r][c]

        return dp[-1]