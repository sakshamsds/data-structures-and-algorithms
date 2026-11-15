class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def bfs(r, c):
            perimeter = 0
            q = deque([(r, c)])
            visited = set([(r, c)])
            while q:
                r, c = q.popleft()
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if (
                        nr < 0 or nr == rows or
                        nc < 0 or nc == cols or
                        grid[nr][nc] == 0
                    ):
                        perimeter += 1
                        continue
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))
            return perimeter

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return bfs(r, c)

        return -1