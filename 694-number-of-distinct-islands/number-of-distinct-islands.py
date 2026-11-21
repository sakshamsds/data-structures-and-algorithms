class Solution:
    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        # use local corrdinates to create hash
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r < 0 or r == rows or 
                c < 0 or c == cols or 
                (r, c) in visited or 
                grid[r][c] == 0
            ):
                return
            visited.add((r, c))
            currentIsland.add((r - rowOrigin, c - colOrigin))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        visited = set()
        uniqueIslands = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 or (r, c) in visited:
                    continue
                currentIsland = set()
                rowOrigin, colOrigin = r, c
                dfs(r, c)
                if currentIsland not in uniqueIslands:
                    uniqueIslands.add(frozenset(currentIsland))

        return len(uniqueIslands)