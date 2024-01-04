class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_max = [0] * n
        col_max = [0] * n

        for r in range(n):
            for c in range(n):
                row_max[r] = max(grid[r][c], row_max[r])
                col_max[c] = max(grid[r][c], col_max[c])

        total_increment = 0
        for r in range(n):
            for c in range(n):
                total_increment += max(0, \
                                       min(row_max[r], col_max[c]) - grid[r][c])
        return total_increment         

        