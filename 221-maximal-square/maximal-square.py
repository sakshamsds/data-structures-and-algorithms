class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [0] * (cols + 1)
        maxSize = 0

        for r in range(rows):
            newDp = [0] * (cols + 1)
            for c in range(cols):
                if matrix[r][c] == '0':
                    continue
                newDp[c + 1] = 1 + min(newDp[c], dp[c + 1], dp[c])
                maxSize = max(maxSize, newDp[c + 1])
            # print(newDp)
            dp = newDp

        return maxSize * maxSize