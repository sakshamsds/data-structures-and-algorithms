class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        # rightmost one 
        n = len(grid)
        pos = [-1] * n
        for r in range(n):
            for c in range(n - 1, -1, -1):
                if grid[r][c] == 1:
                    pos[r] = c
                    break

        # among all that works, find the closest one
        steps = 0
        for cur in range(n):
            found = False
            for nxt in range(cur, n):
                if pos[nxt] <= cur:
                    steps += nxt - cur
                    found = True
                    break
            if not found:
                return -1
            else:
                for i in range(nxt, cur, - 1):
                    pos[i], pos[i - 1] = pos[i - 1], pos[i]

        return steps