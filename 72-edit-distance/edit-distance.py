'''
dp[horse, ros] = 1 + min(dp[hors, ros], dp[horse, ro], dp[hors, ro])
	  0 h o r s e
	0 0	1 2 3 4 5
	r 1 1 2 2 3 4
	o 2 2 1 2 3 4
	s 3 3 2 2 2 3   
add 
delete
rep
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        prev_dp = [i for i in range(m + 1)]

        for r in range(n):
            new_dp = [r + 1] + [float('inf')] * m
            for c in range(m):
                increment = 0 if word2[r] == word1[c] else 1
                new_dp[c + 1] = min(
                    new_dp[c] + 1,
                    prev_dp[c + 1] + 1,
                    prev_dp[c] + increment
                )
            prev_dp = new_dp
        return prev_dp[-1]