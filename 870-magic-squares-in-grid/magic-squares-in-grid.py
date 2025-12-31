class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # sum = 15

        nr, nc = len(grid), len(grid[0])
        if nr < 3 or nc < 3:
            return 0

        allowed_nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        allowed_sum = 15 
        res = 0

        for r in range(nr - 2):
            for c in range(nc - 2):
                sums = set()

                # row_sum
                sums.add(grid[r][c] + grid[r][c + 1] + grid[r][c + 2])
                sums.add(grid[r + 1][c] + grid[r + 1][c + 1] + grid[r + 1][c + 2])
                sums.add(grid[r + 2][c] + grid[r + 2][c + 1] + grid[r + 2][c + 2])

                # col_sum
                sums.add(grid[r][c] + grid[r + 1][c] + grid[r + 2][c])
                sums.add(grid[r][c + 1] + grid[r + 1][c + 1] + grid[r + 2][c + 1])
                sums.add(grid[r][c + 2] + grid[r + 1][c + 2] + grid[r + 2][c + 2])

                # diag_sum
                sums.add(grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2])
                sums.add(grid[r + 2][c] + grid[r + 1][c + 1] + grid[r][c + 2])

                # numbers
                nums = set([
                    grid[r][c], grid[r][c + 1], grid[r][c + 2],
                    grid[r + 1][c], grid[r + 1][c + 1], grid[r + 1][c + 2],
                    grid[r + 2][c], grid[r + 2][c + 1], grid[r + 2][c + 2]]
                )
                
                if len(sums) != 1 or sums.pop() != allowed_sum or len(allowed_nums - nums) != 0:
                    continue
                else:
                    res += 1

        return res


    


