'''
    0   a   b   c   d   e
0   0   0   0   0   0   0
a   0   1   1   1   1   1
c   0   1   1   2   2   2
e   0   1   1   2   2   3
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        prev_dp = [0] * (n + 1)     # row 0

        for i in range(1, m + 1):
            next_dp = [0] * (n + 1)
            for j in range(1, n + 1):
                next_dp[j] = max(prev_dp[j], next_dp[j - 1])
                if text1[i - 1] == text2[j - 1]:
                    next_dp[j] = max(next_dp[j], prev_dp[j - 1] + 1)
            prev_dp = next_dp

        return next_dp[-1]