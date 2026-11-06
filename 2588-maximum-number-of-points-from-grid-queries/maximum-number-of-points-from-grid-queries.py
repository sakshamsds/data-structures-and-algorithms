class Solution:
    def maxPoints(self, grid: list[list[int]], queries: list[int]) -> list[int]:
        # sort the queries
        # bfs from existing point for every query

        rows, cols = len(grid), len(grid[0])

        sortedQueries = sorted([(q, i) for i, q in enumerate(queries)])
        points = [0] * len(queries)

        minHeap = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])

        curPoints = 0

        for q, i in sortedQueries:
            while minHeap and minHeap[0][0] < q:
                _, r, c = heapq.heappop(minHeap)
                curPoints += 1

                for dr, dc in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                    nr, nc = r + dr, c + dc
                    if (
                        nr < 0 or nr >= rows or 
                        nc < 0 or nc >= cols or
                        (nr, nc) in visited 
                    ):
                        continue	
                    heapq.heappush(minHeap, (grid[nr][nc], nr, nc))
                    visited.add((nr, nc))

            points[i] = curPoints

        return points
