'''
    many paths tl -> br
    each path has max height
    use the path to minimize the max height

    find all the paths
'''

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # choose the nbr with min height
        visited = set([(0, 0)])
        pq = [(grid[0][0], 0, 0)]
        max_height = grid[0][0]

        while pq:
            h, r, c = heapq.heappop(pq)
            max_height = max(max_height, h)
            if r == n - 1 and c == n - 1:       # reached the last node
                return max_height
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (
                    nr < 0 or nr >= n or
                    nc < 0 or nc >= n or
                    (nr, nc) in visited
                ):
                    continue

                visited.add((r, c))
                heapq.heappush(pq, (grid[nr][nc], nr, nc))

        return -1