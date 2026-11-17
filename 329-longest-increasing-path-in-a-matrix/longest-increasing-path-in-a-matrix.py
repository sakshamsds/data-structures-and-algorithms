class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        dp = {}     # (r, c) -> max path
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r, c)]

            longest = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (        # out of bounds
                    nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or
                    matrix[nr][nc] <= matrix[r][c]
                ):
                    continue
                longest = max(longest, 1 + dfs(nr, nc))

            dp[(r, c)] = longest
            return longest
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in dp:
                    dfs(r, c)

        return max(dp.values())