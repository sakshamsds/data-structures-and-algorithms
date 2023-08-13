# learning concept, multisource bfs

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        q = deque()
        minutes, fresh = 0, 0
        # no need of visited because we are updating the values

        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 2:     
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        neighbors = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        while q and fresh > 0:
            for _ in range(len(q)):        # for loop doesn't update the len
                r, c = q.popleft()
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    # look only for fresh oranges
                    if (
                        nr < 0 or nr >= num_rows or
                        nc < 0 or nc >= num_cols or
                        grid[nr][nc] != 1
                    ):
                        continue
                    grid[nr][nc] = 2    # now rotten
                    q.append((nr, nc))
                    fresh -= 1
            minutes += 1
        # minutes -= 1    # last iteration will not yield any new rotten oranges

        # after rotting process, check if anything is not rotten
        return minutes if  fresh == 0 else -1

        