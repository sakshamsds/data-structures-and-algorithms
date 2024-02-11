class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        cache = {}

        def dfs(i, j, k):
            if j < 0 or j == cols or k < 0 or k == cols:
                return 0 

            if i == rows:
                return 0
            
            if (i, j, k) in cache:
                return cache[(i, j, k)]

            cherries = grid[i][j]
            if j != k:
                cherries += grid[i][k]

            cherries += max(
                dfs(i + 1, j - 1, k - 1),
                dfs(i + 1, j - 1, k),
                dfs(i + 1, j - 1, k + 1),
                dfs(i + 1, j, k - 1),
                dfs(i + 1, j, k),
                dfs(i + 1, j, k + 1),
                dfs(i + 1, j + 1, k - 1),
                dfs(i + 1, j + 1, k),
                dfs(i + 1, j + 1, k + 1)
            )

            cache[(i, j, k)] = cherries
            return cherries
        return dfs(0, 0, cols - 1)