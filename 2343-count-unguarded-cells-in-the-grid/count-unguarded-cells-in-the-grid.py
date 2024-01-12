class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2

        for r, c in guards:         # iterate in 4 directions
            for i in range(r - 1, -1, -1):  # go up
                if grid[i][c] == 1 or grid[i][c] == 2:
                    break
                grid[i][c] = -1

            for i in range(r + 1, m, +1):   # go down
                if grid[i][c] == 1 or grid[i][c] == 2:
                    break
                grid[i][c] = -1

            for i in range(c - 1, -1, -1):  # go left
                if grid[r][i] == 1 or grid[r][i] == 2:
                    break
                grid[r][i] = -1

            for i in range(c + 1, n, +1):   # go right
                if grid[r][i] == 1 or grid[r][i] == 2:
                    break
                grid[r][i] = -1

        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    res += 1
        return res