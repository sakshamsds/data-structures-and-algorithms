class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        q = deque([(0, 0)])     # (removals, r, c)
        removals = [[float('inf')] * cols for _ in range(rows)]
        removals[0][0] = 0

        while q:
            r, c = q.popleft()
            if r == rows - 1 and c == cols - 1:
                return removals[r][c]
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (
                    nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols 
                ):
                    continue
                if removals[r][c] + grid[nr][nc] < removals[nr][nc]:
                    removals[nr][nc] = removals[r][c] + grid[nr][nc]
                    if grid[nr][nc] == 1:
                        q.append((nr, nc))
                    else:
                        q.appendleft((nr, nc))

        return -1