class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        # number of components

        visited = set()
        rows, cols = len(land), len(land[0])

        def dfs(r, c):
            bottom_right[0] = max(bottom_right[0], r)
            bottom_right[1] = max(bottom_right[1], c)
            visited.add((r, c))
            for dr, dc in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
                nr, nc = r + dr, c + dc
                if (
                    nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or
                    land[nr][nc] == 0 or 
                    (nr, nc) in visited
                ):            
                    continue
                dfs(nr, nc)

        res = []
        for r in range(rows):
            for c in range(cols):
                if land[r][c] == 1 and (r, c) not in visited:
                    bottom_right = [r, c]
                    dfs(r, c)
                    res.append([r, c, bottom_right[0], bottom_right[1]])

        return res