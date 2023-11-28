class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        sx, sy, zeros = 0, 0, 0
        m, n = len(grid), len(grid[0])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    sx, sy = r, c
                if grid[r][c] == 0:
                    zeros += 1

        return self.dfs(grid, sx, sy, zeros)
        
    def dfs(self, grid, r, c, zeros):   # return total paths
        if (r < 0 or c < 0 or 
            r >= len(grid) or 
            c >= len(grid[0]) or 
            grid[r][c] == -1):
            return 0
        if grid[r][c] == 2:
            return 1 if zeros == -1 else 0

        grid[r][c] = -1     # make the current cell unvisitable
        zeros -= 1
        totalPaths = self.dfs(grid, r + 1, c, zeros) + \
                    self.dfs(grid, r - 1, c, zeros) + \
                    self.dfs(grid, r, c + 1, zeros) + \
                    self.dfs(grid, r, c - 1, zeros)

        # backtrack
        zeros += 1
        grid[r][c] = 0          # assuming parent cell is zero
        return totalPaths