'''
    dp[i, j] = maximum square length ending at that (i, j)
    dp[i, j] = min(dp[i - 1, j], dp[i, j - 1], dp[i - 1, j - 1]) if (i, j) has 1
'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        prev_dp = [0] + [int(num) for num in matrix[0]]
        mx_sq = max(prev_dp)

        for r in range(1, rows):
            dp = [0] * (cols + 1)
            for c in range(cols):
                if matrix[r][c] == '0':
                    continue
                dp[c + 1] = min(dp[c], prev_dp[c], prev_dp[c + 1]) + 1
                mx_sq = max(mx_sq, dp[c + 1])
            prev_dp = dp

        return mx_sq ** 2