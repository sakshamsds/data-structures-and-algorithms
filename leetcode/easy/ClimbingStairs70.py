# https://leetcode.com/problems/climbing-stairs/
# 70. Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        prev, cur = 1, 1
        for _ in range(n):
            prev, cur = cur, prev + cur

        return prev

    # def climbStairs(self, n: int) -> int:
    #     dp = [0] * (n + 1)
    #     dp[0] = dp[1] = 1

    #     for i in range(2, n + 1):
    #          dp[i] = dp[i-1] + dp[i-2]

    #     # print(dp)
    #     return dp[n]