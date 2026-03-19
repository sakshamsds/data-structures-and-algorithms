class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        prefix = [[[0, 0] for _ in range(cols)] for _ in range(rows)]

        if grid[0][0] == 'X':
            prefix[0][0][0] = 1
        if grid[0][0] == 'Y':
            prefix[0][0][1] = 1

        res = 0
        for c in range(1, cols):
            prefix[0][c][0] = prefix[0][c - 1][0]
            prefix[0][c][1] = prefix[0][c - 1][1]
            if grid[0][c] == 'X':
                prefix[0][c][0] += 1
            if grid[0][c] == 'Y':
                prefix[0][c][1] += 1

            if prefix[0][c][0] > 0 and prefix[0][c][0] == prefix[0][c][1]:
                res += 1

        for r in range(1, rows):
            prefix[r][0][0] = prefix[r - 1][0][0]
            prefix[r][0][1] = prefix[r - 1][0][1]
            if grid[r][0] == 'X':
                prefix[r][0][0] += 1
            if grid[r][0] == 'Y':
                prefix[r][0][1] += 1
        
            if prefix[r][0][0] > 0 and prefix[r][0][0] == prefix[r][0][1]:
                res += 1

        for r in range(1, rows):
            for c in range(1, cols):    
                prefix[r][c][0] = prefix[r - 1][c][0] + prefix[r][c - 1][0] - prefix[r - 1][c - 1][0]
                prefix[r][c][1] = prefix[r - 1][c][1] + prefix[r][c - 1][1] - prefix[r - 1][c - 1][1]

                if grid[r][c] == 'X':
                    prefix[r][c][0] += 1
                if grid[r][c] == 'Y':
                    prefix[r][c][1] += 1

                if prefix[r][c][0] > 0 and prefix[r][c][0] == prefix[r][c][1]:
                    res += 1

        return res