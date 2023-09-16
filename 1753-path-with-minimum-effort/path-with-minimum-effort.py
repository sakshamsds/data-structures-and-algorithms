class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        # heap with tuple (cur_max_diff, r, c)
        heap = [(0, 0, 0)]
        visited = set()
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        # greedy bfs/dijkstra
        while heap:
            cur_max_diff, r, c = heapq.heappop(heap)
            # print(r, c, cur_max_diff)
            if (r, c) in visited:               # base case 1
                continue
            visited.add((r, c))
            if r == rows - 1 and c == cols - 1:     # base case 2, reached the end
                return cur_max_diff

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (                                # validate neighbor
                    nr < 0 or nr == rows or
                    nc < 0 or nc == cols or
                    (nr, nc) in visited
                ):
                    continue
                new_diff = max(cur_max_diff, abs(heights[nr][nc] - heights[r][c]))
                heapq.heappush(heap, (new_diff, nr, nc))

        return 0