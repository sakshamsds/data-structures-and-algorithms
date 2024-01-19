class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]

        for r in range(1, n):
            matrix[r][0] += min(matrix[r - 1][0], matrix[r - 1][1])
            matrix[r][-1] += min(matrix[r - 1][-1], matrix[r - 1][-2])
            for c in range(1, n - 1):
                 matrix[r][c] += min(matrix[r - 1][c - 1],
                                     matrix[r - 1][c],
                                     matrix[r - 1][c + 1])
    
        return min(matrix[-1])