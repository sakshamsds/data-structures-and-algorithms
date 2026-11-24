class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        # mark one island as 2
        # add those in queue
        # multisource bfs to find the nearest 1

        rows, cols = len(grid), len(grid[0])
        q = deque()

        def dfs(r, c):
            if (
                r < 0 or r == rows or
                c < 0 or c == cols or 
                grid[r][c] != 1
            ):
                return
            q.append((r, c))
            grid[r][c] = 2
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        def markTwos():
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1:
                        dfs(r, c)
                        return
        markTwos()

        flips = 0
        visited = set(q)
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if (
                        nr < 0 or nr == rows or 
                        nc < 0 or nc == cols or
                        (nr, nc) in visited
                    ):
                        continue
                    if grid[nr][nc] == 1:       # reached other island
                        return flips
                    q.append((nr, nc))
                    visited.add((nr, nc))
            flips += 1
        return -1