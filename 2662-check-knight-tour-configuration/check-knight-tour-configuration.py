class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)

        if grid[0][0] != 0:
            return False

        directions = [
            (1, 2), (2, 1), (2, -1), (1, -2),
            (-1, -2), (-2, -1), (-2, 1), (-1, 2)
        ]


        def dfs(r, c, num_pos):
            if (r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != num_pos):
                return False
            if num_pos == n * n - 1:
                return True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc, num_pos + 1):
                    return True
            return False
        
        return dfs(0, 0, 0)



        