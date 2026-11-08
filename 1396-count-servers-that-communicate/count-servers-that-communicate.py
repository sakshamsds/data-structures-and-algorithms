class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        # TC - O(N * M), two pass
        # SC - O(n + m)
        rows, cols = len(grid), len(grid[0])

        rowCount = [0] * rows
        colCount = [0] * cols

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    rowCount[r] += 1
                    colCount[c] += 1
        
        connected = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if rowCount[r] > 1 or colCount[c] > 1:
                        connected += 1
        return connected