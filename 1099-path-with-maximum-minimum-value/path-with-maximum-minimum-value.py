class Solution:
    def maximumMinimumPath(self, grid: list[list[int]]) -> int:
        # greedy bfs, select nbr with max value
        maxHeap = [(-grid[0][0], 0, 0)]      # val, r, c
        rows, cols = len(grid), len(grid[0])
        visited = set([(0, 0)])

        minVal = grid[0][0]
        while maxHeap:
            val, r, c = heapq.heappop(maxHeap)
            val = -val
            minVal = min(minVal, val)
            if r == rows - 1 and c == cols - 1:
                return minVal

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (
                    nr < 0 or nr == rows or 
                    nc < 0 or nc == cols or
                    (nr, nc) in visited
                ):
                    continue
                heapq.heappush(maxHeap, (-grid[nr][nc], nr, nc))
                visited.add((nr, nc))
        return minVal

