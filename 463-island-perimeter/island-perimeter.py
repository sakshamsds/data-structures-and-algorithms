class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(r, c):
            perimeter = 0
            visited.add((r, c))
            for dr, dc in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or
                    grid[nr][nc] == 0):
                    perimeter += 1
                elif (nr, nc) not in visited:
                    perimeter += dfs(nr, nc)
            return perimeter

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c)

        return -1