class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        q = deque([(grid[0][0], 0, 0)])     # (removals, r, c)
        visited = set()

        while q:
            removals, r, c = q.popleft()
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if r == rows - 1 and c == cols - 1:
                return removals
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (
                    nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or
                    (nr, nc) in visited
                ):
                    continue
                if grid[nr][nc] == 1:
                    q.append((removals + grid[nr][nc], nr, nc))
                else:
                    q.appendleft((removals, nr, nc))

        return -1