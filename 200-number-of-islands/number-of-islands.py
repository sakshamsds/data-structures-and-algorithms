class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            visited.add((r, c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                if (
                    nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or
                    grid[nr][nc] == '0' or
                    (nr, nc) in visited 
                ):
                    continue
                dfs(nr, nc)

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    res += 1
                    dfs(r, c)

        return res

            