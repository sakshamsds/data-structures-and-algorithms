class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        # multi source bfs
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = -1
                    q.append((r, c))

        safeDist = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                    nr, nc = r + dr, c + dc
                    if (
                        nr < 0 or nr == rows or 
                        nc < 0 or nc == cols or
                        grid[nr][nc] != 0
                    ):
                        continue
                    grid[nr][nc] = safeDist
                    q.append((nr, nc))
            safeDist += 1
        
        # for row in grid:
            # print(row)

        # greedy bfs from the top
        visited = set()
        minSafety = grid[0][0]
        maxHeap = [(-grid[0][0], 0, 0)]
        while maxHeap:
            safeDist, r, c = heapq.heappop(maxHeap)
            minSafety = min(minSafety, -safeDist)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if r == rows - 1 and c == cols - 1:     # reached bottom right
                break
            for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nr, nc = r + dr, c + dc
                if (
                    nr < 0 or nr == rows or 
                    nc < 0 or nc == cols or
                    (nr, nc) in visited
                ):
                    continue
                heapq.heappush(maxHeap, (-grid[nr][nc], nr, nc))

        return 0 if minSafety == -1 else minSafety 