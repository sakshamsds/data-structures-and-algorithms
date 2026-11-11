class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ways = [0] * cols
        ways[0] = 1
        
        for r in range(rows):
            if grid[r][0] == 1:     # if this is blocked
                ways[0] = 0
            for c in range(1, cols):
                if grid[r][c] == 1:
                    ways[c] = 0
                else:
                    ways[c] += ways[c - 1]

        return ways[-1]