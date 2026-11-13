class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        # greedily choose the nbr with min height difference
        directions = [
            (0, 1),     # right
            (1, 0),     # bottom
            (0, -1),    # left
            (-1, 0)     # top
        ]
        visited = set()
        minHeap = [(0, 0, 0)]   # effort, r, c
        while minHeap:
            effort, r, c = heapq.heappop(minHeap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if r == rows - 1 and c == cols - 1:
                return effort
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    nr < 0 or nr == rows or
                    nc < 0 or nc == cols or
                    (nr, nc) in visited
                ):
                    continue
                nbrEffort = max(effort, abs(heights[nr][nc] - heights[r][c]))
                heapq.heappush(minHeap, (nbrEffort, nr, nc))
        
        return -1