class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        res = []
        for c in range(n):  # get all columns as rows in res
            row = []
            for r in range(m):
                row.append(matrix[r][c])
            res.append(row)
        return res