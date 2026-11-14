'''
    TC - O(mnlogmnk)
    SC - O(mnk)
'''

class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])

        if k >= rows + cols - 2:
            return rows + cols - 2
        
        visited = {(0, 0): 0}       # minimum deletions used to reach
        minHeap = [(0, 0, 0, 0)]     # steps, deletions, r, c

        while minHeap:
            steps, deletions, r, c = heapq.heappop(minHeap)
            if r == rows - 1 and c == cols - 1:
                return steps
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    newDeletions = deletions + grid[nr][nc]
                    if newDeletions <= k:
                        if (nr, nc) not in visited or visited[(nr, nc)] > newDeletions:
                            heapq.heappush(minHeap, (steps + 1, newDeletions, nr, nc))
                            visited[(nr, nc)] = newDeletions

        return -1