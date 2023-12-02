class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        total_area = 0
        for r in range(n):
            row_area = 0
            col_area = 0
            floor_area = 0
            for c in range(n):
                row_area = max(row_area, grid[r][c])
                col_area = max(col_area, grid[c][r])
                if grid[r][c] > 0:
                    floor_area += 1
            total_area += row_area + col_area + floor_area
        return total_area
