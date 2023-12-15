class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        onesRow = [0] * m
        onesCol = [0] * n
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    onesRow[r] += 1
                    onesCol[c] += 1

        diff = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                diff[r][c] = 2 * onesRow[r] + 2 * onesCol[c] - m - n

        return diff
