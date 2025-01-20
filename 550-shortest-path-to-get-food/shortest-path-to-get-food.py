class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # find start point
        sr, sc = -1, -1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "*":
                    sr, sc = r, c
                    break

        # bfs
        q = collections.deque()
        visited = set()
        q.append((sr, sc))
        dist = 0

        while q:
            dist += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if (
                        nr < 0 or nr >= rows or
                        nc < 0 or nc >= cols or
                        grid[nr][nc] == "X" or
                        (nr, nc) in visited 
                    ):
                        continue
                    if grid[nr][nc] == "#":
                        return dist
                    q.append((nr, nc))
                    visited.add((nr, nc))

        return -1
