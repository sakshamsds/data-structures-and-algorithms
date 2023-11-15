class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        pq = [(0, 0, 0)]       # (effort, r, c)
        visited = set()

        while pq:
            cur_effort, r, c = heapq.heappop(pq)

            if (r, c) in visited:
                continue

            visited.add((r, c))

            if (r, c) == (rows - 1, cols - 1):
                return cur_effort

            for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nr, nc = r + dr, c + dc

                # validate nbr
                if (nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or
                    (nr, nc) in visited):
                    continue

                effort = max(cur_effort, abs(heights[nr][nc] - heights[r][c]))
                heapq.heappush(pq, (effort, nr, nc))

        return -1