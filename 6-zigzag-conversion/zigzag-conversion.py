class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        grid = [[] for _ in range(numRows)]
        row, direction = 0, 1       # 1 is down, -1 is up
        for c in s:
            grid[row].append(c)
            row += direction
            if row == numRows:
                direction = -1
                row = numRows - 2
            if row == -1:
                direction = 1
                row = 1

        # print(grid)
        res = []
        for row in grid:
            res.extend(row)

        return ''.join(res)