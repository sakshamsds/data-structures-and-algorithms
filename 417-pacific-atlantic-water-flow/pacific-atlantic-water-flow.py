class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def bfs(q, visited):
            while q:
                r, c = q.popleft()
                for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if (
                        nr < 0 or nr >= rows or
                        nc < 0 or nc >= cols or
                        (nr, nc) in visited or
                        heights[nr][nc] < heights[r][c]
                    ):
                        continue
                    q.append((nr, nc))
                    visited.add((nr, nc))
            return visited

        pacificCells = deque()
        atlanticCells = deque()
        for c in range(cols):
            pacificCells.append((0, c))
            atlanticCells.append((rows - 1, c))
        for r in range(1, rows):
            pacificCells.append((r, 0))
            atlanticCells.append((r - 1, cols - 1))

        pacificSet = bfs(pacificCells, set(pacificCells))
        atlanticSet = bfs(atlanticCells, set(atlanticCells))

        return list(pacificSet.intersection(atlanticSet))