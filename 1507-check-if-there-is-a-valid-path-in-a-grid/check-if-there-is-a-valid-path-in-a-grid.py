class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # Up: (-1, 0), Down: (1, 0), Left: (0, -1), Right: (0, 1)
        directions = {
            1 : [(0, -1), (0, 1)],   # Left, Right
            2 : [(-1, 0), (1, 0)],   # Up, Down
            3 : [(0, -1), (1, 0)],   # Left, Down
            4 : [(0, 1), (1, 0)],    # Right, Down
            5 : [(0, -1), (-1, 0)],  # Left, Up
            6 : [(0, 1), (-1, 0)],   # Right, Up
        }

        ROWS, COLS = len(grid), len(grid[0])

        q = deque([(0, 0)])
        visited = set([(0, 0)])

        while q:
            r, c = q.popleft()
            if (r, c) == (ROWS - 1, COLS - 1):
                return True

            for dr, dc in directions[grid[r][c]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (-dr, -dc) in directions[grid[nr][nc]] and (nr, nc) not in visited:
                    visited.add((r, c))
                    q.append((nr, nc))

        return False