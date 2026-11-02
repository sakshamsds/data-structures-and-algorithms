class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        # make all points on 1 island as 2
        # run bfs
        # TC - O(n**2), SC - O(n)

        bfs_queue = deque()
        visited = set()
        n = len(grid)

        def dfs(r, c):
            if (
                r < 0 or r >= n or
                c < 0 or c >= n or
                grid[r][c] != 1
            ):
                return 
            grid[r][c] = 2
            bfs_queue.append((r, c)) 
            visited.add((r, c))               
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        def makeTwos():
            for r in range(n):
                for c in range(n):
                    if grid[r][c] == 1:
                        dfs(r, c)
                        return
        makeTwos()

        distance = 0
        while bfs_queue:
            for _ in range(len(bfs_queue)):
                r, c = bfs_queue.popleft()
                for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if (
                        nr < 0 or nr >= n or
                        nc < 0 or nc >= n or
                        (nr, nc) in visited
                    ):
                        continue
                    bfs_queue.append((nr, nc))
                    visited.add((nr, nc))
                    if grid[nr][nc] == 1:
                        return distance
            distance += 1
        return distance        