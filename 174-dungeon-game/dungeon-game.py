class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * (cols + 1) for _ in range(rows + 1)]
        dp[rows - 1][cols] = 1

        # calculate min val for each cell
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                dp[r][c] = max(1, min(dp[r][c + 1], dp[r + 1][c]) - dungeon[r][c])

        return dp[0][0]

