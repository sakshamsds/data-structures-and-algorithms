'''
            a   c   e
        0   0   0   0
    a   0   1   1   1
    b   0   1   1   1
    c   0   1   2   2      
    d   0   1   2   2
    e   0   1   2   3

ac, ab
a, ab
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        prev_dp = [0] * (len(text2) + 1)

        for r in range(len(text1)):
            new_dp = [0] * (len(text2) + 1)
            for c in range(1, len(text2) + 1):
                increment = 1 if text1[r] == text2[c - 1] else 0
                new_dp[c] = max(
                    new_dp[c - 1], 
                    prev_dp[c], 
                    prev_dp[c - 1] + increment
                )
            prev_dp = new_dp
        return prev_dp[-1]