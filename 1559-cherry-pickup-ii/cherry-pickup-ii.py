class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        cache = {}

        def dfs(r, c1, c2):
            if min(c1, c2) < 0 or max(c1, c2) == cols or r == rows:
                return 0 
            
            if (r, c1, c2) in cache:
                return cache[(r, c1, c2)]

            cherries = 0
            for c1_d in [-1, 0, 1]:
                for c2_d in [-1, 0, 1]:
                    cherries = max(cherries, 
                                    dfs(r + 1, c1 + c1_d, c2 + c2_d))

            cherries += grid[r][c1]
            if c1 != c2:
                cherries += grid[r][c2]

            cache[(r, c1, c2)] = cherries
            return cherries

        return dfs(0, 0, cols - 1)