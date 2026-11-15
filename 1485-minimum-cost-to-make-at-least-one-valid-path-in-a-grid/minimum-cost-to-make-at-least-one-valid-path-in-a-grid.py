class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        # 0-1 BFS
        rows, cols = len(grid), len(grid[0])

        costs = [[float('inf')] * cols for _ in range(rows)]
        costs[0][0] = 0
        q = deque([(0, 0)])

        dirs = {
            1: (0, 1),
            2: (0, -1),
            3: (1, 0),
            4: (-1, 0)
        }

        while q:
            r, c = q.popleft()
            # print(r, c)
            if r == rows - 1 and c == cols - 1:
                return costs[r][c]
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    newCost = costs[r][c] + 1
                    if dirs[grid[r][c]] == (dr, dc):
                        newCost -= 1
                    # cost to reach this nbr
                    if newCost < costs[nr][nc]:
                        costs[nr][nc] = newCost
                        if dirs[grid[r][c]] == (dr, dc):
                            q.appendleft((nr, nc))
                        else:
                            q.append((nr, nc))

        return -1