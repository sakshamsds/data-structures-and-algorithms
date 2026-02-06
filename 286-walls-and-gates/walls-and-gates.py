class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        
        q = deque()
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        dist = 0
        while q:
            dist += 1
            level = len(q)
            for _ in range(level):
                r, c = q.popleft()
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if (
                        nr < 0 or nr >= rows or
                        nc < 0 or nc >= cols or
                        (nr, nc) in visited or
                        rooms[nr][nc] == -1
                    ):
                        continue
                    visited.add((nr, nc))
                    q.append((nr, nc))
                    rooms[nr][nc] = dist