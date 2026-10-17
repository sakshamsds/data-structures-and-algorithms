'''
    [1,1,1,1,1]
    [1,0,0,0,1]
   1[1,0,1,0,1]
    [1,0,0,0,1]
    [1,1,1,1,1]

    # iterate matrix
    # for the first 1, dfs to mark all the points 2
    # rem is 1
    # bfs from every point edge in 2 to closest distance to 1
'''

class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        n = len(grid)

        def dfs(r, c):
            if (r < 0 or r >= n or 
                c < 0 or c >= n or  
                grid[r][c] != 1):
                    return
            grid[r][c] = 2
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        def make_twos():
            for r in range(n):
                for c in range(n):
                    if grid[r][c] == 1:
                        dfs(r, c)
                        return

        make_twos()
        # print(grid)

        def bfs(start_r, start_c):
            visited = set(((start_r, start_c)))
            queue = deque([(start_r, start_c)])
            flips = -1
            while queue:
                flips += 1
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = r + dr, c + dc
                        if (
                            nr < 0 or nr >= n or
                            nc < 0 or nc >= n or
                            (nr, nc) in visited or 
                            grid[nr][nc] == 2          
                        ):
                            continue
                        if grid[nr][nc] == 1:
                            return flips
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return n * n

        min_flips = n * n
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 2:
                    # bfs to nearest 1
                    min_flips = min(min_flips, bfs(r, c))

        return min_flips


                        

            