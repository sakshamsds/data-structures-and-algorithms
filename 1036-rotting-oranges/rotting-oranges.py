class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # multi source bfs
        # all 2s go in the queue

        q = deque()
        freshOranges = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    freshOranges += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        minutes = 0
        while q:
            if freshOranges == 0:
                return minutes
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if (
                        nr < 0 or nr >= rows or
                        nc < 0 or nc >= cols or
                        grid[nr][nc] != 1
                    ):
                        continue
                    freshOranges -= 1
                    q.append((nr, nc))
                    grid[nr][nc] = 2
            minutes += 1

        return minutes if freshOranges == 0 else -1
