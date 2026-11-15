class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        # 0-1 bfs
        rows, cols = len(grid), len(grid[0])

        q = deque()       # remHealth, r, c
        q.append((health - grid[0][0], 0, 0))
        visited = set([(0, 0)])

        while q:
            remHealth, r, c = q.popleft()
            if remHealth == 0:
                continue
            if r == rows - 1 and c == cols - 1:
                return True
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (
                    nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or
                    (nr, nc) in visited
                ):
                    continue
                
                if grid[nr][nc] == 0:
                    q.appendleft((remHealth, nr, nc))
                else:
                    q.append((remHealth - 1, nr, nc))
                visited.add((nr, nc))

        return False