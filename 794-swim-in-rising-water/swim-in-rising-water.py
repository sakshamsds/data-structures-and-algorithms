class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        # minimize the max height along the path

        min_heap = [(grid[0][0], 0, 0)]		# (max_height in the path, r, c)
        rows, cols = len(grid), len(grid[0])
        visited = set([(0, 0)])

        while min_heap:
            cur_max, r, c = heapq.heappop(min_heap)
            if (r, c) == (rows - 1, cols - 1):
                return cur_max

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if ( 
                    nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or
                    (nr, nc) in visited
                ):
                    continue
                new_max = max(cur_max, grid[nr][nc])	
                visited.add((nr, nc))		
                heapq.heappush(min_heap, (new_max, nr, nc))

        return -1