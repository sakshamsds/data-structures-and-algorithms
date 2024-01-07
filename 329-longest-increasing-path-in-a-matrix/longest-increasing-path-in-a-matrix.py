class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # store longest path at each matrix entry
        rows, cols = len(matrix), len(matrix[0])
        cache = {}
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if (r, c) in cache:
                return cache[(r, c)]
            
            path_length = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or
                    matrix[nr][nc] <= matrix[r][c]
                ):
                    continue
                path_length = max(path_length, 1 + dfs(nr, nc))

            cache[(r, c)] = path_length
            return path_length

        longest = 0
        for r in range(rows):
            for c in range(cols):
                longest = max(longest, dfs(r, c))   
        
        # print(cache)
        return longest