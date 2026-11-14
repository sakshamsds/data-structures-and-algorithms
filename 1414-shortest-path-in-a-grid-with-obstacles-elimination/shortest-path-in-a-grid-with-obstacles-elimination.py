'''
    TC - O(M*N*K)
    SC - O(M*N*K)
'''

class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        state = (0, 0, 0)
        q.append(state)
        visited = set([state])

        # optimization
        if k >= rows + cols - 2:
            return rows + cols - 2

        steps = 0
        while q:
            for _ in range(len(q)):
                r, c, deletions = q.popleft()
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if (
                        nr < 0 or nr == rows or
                        nc < 0 or nc == cols or 
                        (nr, nc, deletions + grid[nr][nc]) in visited or
                        (deletions == k and grid[nr][nc] == 1)      # can't traverse
                    ):
                        continue

                    if nr == rows - 1 and nc == cols - 1:
                        return steps + 1
                    
                    newState = (nr, nc, deletions + grid[nr][nc])
                    visited.add(newState)
                    q.append(newState)
            steps += 1

        return -1