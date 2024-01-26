class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # dp = [[0] * n for _ in range(m)]
        dp = {}

        def dfs(r, c, moves):
            if moves > maxMove:
                return 0

            # out of bounds
            if moves <= maxMove and (r < 0 or c < 0 or r >= m or c >= n):
                return 1

            if (r, c, moves) in dp:
                return dp[(r, c, moves)]

            paths = 0
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                paths += dfs(nr, nc, moves + 1)
                paths = paths % (10 ** 9 + 7)

            dp[(r, c, moves)] = paths
            return paths

        return dfs(startRow, startColumn, 0)
