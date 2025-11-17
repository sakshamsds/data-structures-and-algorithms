class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        
        grid = [[0] * (n + 1) for _ in range(n + 1)]

        for r1, c1, r2, c2 in queries:
            grid[r1][c1] += 1
            grid[r1][c2 + 1] -= 1
            grid[r2 + 1][c1] -= 1
            grid[r2 + 1][c2 + 1] += 1


        for r in range(n):
            for c in range(n):
                top = 0 if r == 0 else grid[r - 1][c]
                left = 0 if c == 0 else grid[r][c - 1]
                top_left = 0 if r == 0 or c == 0 else grid[r - 1][c - 1]
                grid[r][c] += top + left - top_left

        grid = grid[:-1]    # remove last row
        return [row[:-1] for row in grid]       # remove last column
    
        
