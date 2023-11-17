class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dfs from ocean
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited):
            if (r, c) in visited:
                return 

            visited.add((r, c))
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (
                    nr < 0 or rows <= nr or
                    nc < 0 or cols <= nc or
                    (nr, nc) in visited or       # they already have pacific flow
                    heights[nr][nc] < heights[r][c]
                ):
                    continue
                dfs(nr, nc, visited)

        for c in range(cols):
            dfs(0, c, pac)
            dfs(rows - 1, c, atl)

        for r in range(rows):
            dfs(r, 0, pac)
            dfs(r, cols - 1, atl)

        return list(pac & atl)