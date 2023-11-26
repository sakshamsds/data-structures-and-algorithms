class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(1, n):   # iterate rows
            matrix[i][0] += min(matrix[i - 1][0], matrix[i - 1][1])
            matrix[i][-1] += min(matrix[i - 1][-1], matrix[i - 1][-2])
            for j in range(1, n - 1):
                matrix[i][j] += min(matrix[i - 1][j - 1],
                                 matrix[i - 1][j],
                                 matrix[i - 1][j + 1])

        return min(matrix[-1])