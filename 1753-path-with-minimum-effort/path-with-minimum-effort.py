class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        min_heap = [(0, 0, 0)]      # max effort encountered so far
        visited = set()
        rows, cols = len(heights), len(heights[0])
        
        while min_heap:
            effort, r, c = heapq.heappop(min_heap)
            if (r, c) in visited:
                continue
            visited.add((r, c))

            if r == rows - 1 and c == cols - 1:
                return effort
            
            for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or 
                    (nr, nc) in visited):
                    continue
                
                max_current_effort = max(
                    effort, 
                    abs(heights[nr][nc] - heights[r][c])
                )
                heapq.heappush(min_heap, (max_current_effort, nr, nc))
                
        return -1
