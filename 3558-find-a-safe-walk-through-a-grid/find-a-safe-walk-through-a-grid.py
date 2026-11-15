class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        # 0-1 bfs
        rows, cols = len(grid), len(grid[0])

        q = deque()       # remHealth, r, c
        q.append((health - grid[0][0], 0, 0))
        visited = {
            (0, 0): health
        }

        while q:
            remHealth, r, c = q.popleft()
            if r == rows - 1 and c == cols - 1:
                return True
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    nextHealth = remHealth - grid[nr][nc]
                    if nextHealth > 0 and nextHealth > visited.get((nr, nc), 0):
                        visited[(nr, nc)] = nextHealth
                        
                        if grid[nr][nc] == 0:
                            q.appendleft((nextHealth, nr, nc))
                        else:
                            q.append((nextHealth, nr, nc))

        return False