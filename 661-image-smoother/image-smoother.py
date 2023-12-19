class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        points = [(0, 0), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1), (-1, 1), (-1, 0), (-1, -1)]
        res = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                agg, cnt = 0, 0
                for dr, dc in points:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols):
                        agg += img[nr][nc]
                        cnt += 1
                res[r][c] = agg // cnt
        return res