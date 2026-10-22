'''
            a   b   c   d   e
        0   0   0   0   0   0
    a   0   1   1   1   1   1     
    c   0   1   1   2   2   2
    e   9
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cols, rows = len(text1), len(text2)
        dp = [0] * (cols + 1)

        for r in range(rows):
            new_dp = [0] * (cols + 1)
            for c in range(cols):
                increment = 1 if text1[c] == text2[r] else 0
                new_dp[c + 1] = max(dp[c + 1], new_dp[c], increment + dp[c])
            dp = new_dp

        return dp[-1]