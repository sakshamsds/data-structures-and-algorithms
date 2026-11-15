class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        next_dp = [float('inf')] * (cols + 1)
        next_dp[-2] = 1

        # calculate min val for each cell
        for r in range(rows - 1, -1, -1):
            cur_dp = [float('inf')] * (cols + 1) 
            for c in range(cols - 1, -1, -1):
                cur_dp[c] = max(1, min(cur_dp[c + 1], next_dp[c]) - dungeon[r][c])
            next_dp = cur_dp

        return next_dp[0]

