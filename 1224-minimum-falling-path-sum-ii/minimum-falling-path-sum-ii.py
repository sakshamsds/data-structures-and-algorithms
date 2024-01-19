class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)

        for r in range(1, n):
            for c in range(n):
                grid[r][c] += min(grid[r - 1][0:c] + grid[r - 1][c + 1:])

        return min(grid[-1])