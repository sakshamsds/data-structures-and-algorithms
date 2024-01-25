'''
    -   a   b   c   d   e   e
-   0   0   0   0   0   0   0
a   0   1   1   1   1   1   1
c   0   1   1   2   2   2   2
e   0   1   1   2   2   3   3

abcd[e]
ac[e]

abcde
ac[e]

abcd[e]
ace
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)
        for i in range(m):
            new_dp = [0] * (n + 1)
            for j in range(1, n + 1):
                incre = 1 if text1[i] == text2[j - 1] else 0
                new_dp[j] = max(new_dp[j - 1], dp[j], dp[j - 1] + incre)
            dp = new_dp
        return new_dp[-1]
