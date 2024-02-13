class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        mx_sum = -1
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                cur_sum = grid[r][c]
                for dr, dc in product([-1, 1], [-1, 0, 1]):
                    cur_sum += grid[r + dr][c + dc]
                mx_sum = max(mx_sum, cur_sum)
        return mx_sum