class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        rows, cols = len(grid2), len(grid2[0])
        cnt_sub_islands = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid2[r][c] == 0:
                return
            grid2[r][c] = 0
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

        # remove islands
        for r, c in itertools.product(range(rows), range(cols)):
            if grid2[r][c] == 1 and grid1[r][c] == 0:
                dfs(r, c)

        # cnt remaining
        for r, c in itertools.product(range(rows), range(cols)):
            if grid2[r][c] == 1:
                dfs(r, c)
                cnt_sub_islands += 1

        return cnt_sub_islands
