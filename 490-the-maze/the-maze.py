'''
1   1   1   1   1   1   1
1   0   E   1   0   S   1
1   0   0   0   0   0   1
1   0   0   0   1   0   1
1   1   1   0   1   1   1
1   0   0   0   0   0   1
1   1   1   1   1   1   1
'''


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = set()
        rows, cols = len(maze), len(maze[0])

        def dfs(r, c):
            if (r, c) in visited:
                return False

            if [r, c] == destination:
                return True

            visited.add((r, c))

            # move down
            next_r = r
            while next_r + 1 < rows and maze[next_r + 1][c] == 0:
                next_r += 1

            # move up
            prev_r = r
            while prev_r - 1 >= 0 and maze[prev_r - 1][c] == 0:
                prev_r -= 1

            # move right
            next_c = c
            while next_c + 1 < cols and maze[r][next_c + 1] == 0:
                next_c += 1

            # move left
            prev_c = c
            while prev_c - 1 >= 0 and maze[r][prev_c - 1] == 0:
                prev_c -= 1

            return dfs(next_r, c) or \
                    dfs(prev_r, c) or \
                    dfs(r, next_c) or \
                    dfs(r, prev_c)

        return dfs(start[0], start[1])