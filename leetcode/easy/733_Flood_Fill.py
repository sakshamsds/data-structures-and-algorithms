from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        num_rows, num_cols = len(image), len(image[0])
        visited = set()
        p_color = image[sr][sc]

        def dfs(r, c):
            if (
                r < 0 or r >= num_rows or
                c < 0 or c >= num_cols or
                image[r][c] != p_color or
                (r, c) in visited
            ):
                return
            visited.add((r, c))
            image[r][c] = color
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
            return

        dfs(sr, sc)

        return image