'''
delete
leet

lee
let

delete i, i + 1
delete j, j + 1
don't delete only if equal, i + 1, j + 1

dp(del, le) = min(
                dp(de, le) + ord(l),
                dp(del, l) + ord(e),
                dp(de, l) + ord(l) + ord(e)     # both l and e are same then no addition
            ) 

        d   e   l   e   t   e
    0   1   2   3   4   5   6
l   1   2   3   
e   2   3       
e   3
t   4

dp[i][j] = min(top + del_i, left + del_j)
if si = sj, top_left + 0
if s1 != sj, top_left + 2
'''


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        prev_dp = [0]
        for i in range(len(s1)):
            prev_dp.append(ord(s1[i]) + prev_dp[-1])
        # print(prev_dp)

        for i in range(len(s2)):
            dp = [0] * (len(s1) + 1)
            dp[0] = ord(s2[i]) + prev_dp[0]

            for j in range(1, len(s1) + 1):
                top_left = prev_dp[j - 1]
                top_left += 0 if s1[j - 1] == s2[i] else ord(s1[j - 1]) + ord(s2[i]) 
                dp[j] = min(prev_dp[j] + ord(s2[i]), dp[j - 1] + ord(s1[j - 1]), top_left)

            prev_dp = dp
        return dp[-1]