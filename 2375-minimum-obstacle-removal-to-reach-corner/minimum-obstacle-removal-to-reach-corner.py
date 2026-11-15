class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visited = set()
        minHeap = [(0, 0, 0)]      # removals, r, c

        while minHeap:
            removals, r, c = heapq.heappop(minHeap)
            if r == rows - 1 and c == cols - 1:
                return removals
            if (r, c) in visited:
                continue
            visited.add((r, c))

            for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nr, nc = r + dr, c + dc
                if (
                    nr < 0 or nr >= rows or 
                    nc < 0 or nc >= cols or
                    (nr, nc) in visited
                ):
                    continue
                heapq.heappush(minHeap, (removals + grid[nr][nc], nr, nc))

        return -1
