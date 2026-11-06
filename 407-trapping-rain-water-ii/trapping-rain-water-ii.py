class Solution:
    def trapRainWater(self, heights: list[list[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        # start with the boundary heights
        minHeap = []  # (height, r, c)
        for r in range(rows):
            minHeap.append((heights[r][0], r, 0))
            minHeap.append((heights[r][cols - 1], r, cols - 1))

        for c in range(1, cols - 1):
            minHeap.append((heights[0][c], 0, c))
            minHeap.append((heights[rows - 1][c], rows - 1, c))

        heapq.heapify(minHeap)
        visited = set([(r, c) for h, r, c in minHeap])

        trappedWater = 0
        while minHeap:
            height, r, c = heapq.heappop(minHeap)

            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr, nc) in visited:
                    continue

                # can we trap water for this nbr
                if heights[nr][nc] < height:
                    trappedWater += height - heights[nr][nc]
                    heapq.heappush(minHeap, (height, nr, nc))
                else:
                    heapq.heappush(minHeap, (heights[nr][nc], nr, nc))
                visited.add((nr, nc))

        return trappedWater
