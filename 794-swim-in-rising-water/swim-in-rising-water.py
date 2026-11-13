class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        # max height that we traversed 
        n = len(grid)

        visited = set()
        minHeap = [(grid[0][0], 0, 0)]      # height, r, c
        while minHeap:
            height, r, c = heapq.heappop(minHeap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if r == n - 1 and c == n - 1:
                return height

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (
                    nr < 0 or nr == n or 
                    nc < 0 or nc == n or
                    (nr, nc) in visited
                ):
                    continue
                maxHeight = max(height, grid[nr][nc])
                heapq.heappush(minHeap, (maxHeight, nr, nc))

        return -1