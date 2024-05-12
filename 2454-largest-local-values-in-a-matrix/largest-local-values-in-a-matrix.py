class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        mx_grid = [[0] * (n - 2) for _ in range(n - 2)]

        for r in range(1, n - 1):
            for c in range(1, n - 1):
                mx_grid[r - 1][c - 1] = max(
                        grid[r-1][c-1], grid[r-1][c], grid[r-1][c+1],
                        grid[r][c-1], grid[r][c], grid[r][c+1],
                        grid[r+1][c-1], grid[r+1][c], grid[r+1][c+1]
                )
        return mx_grid