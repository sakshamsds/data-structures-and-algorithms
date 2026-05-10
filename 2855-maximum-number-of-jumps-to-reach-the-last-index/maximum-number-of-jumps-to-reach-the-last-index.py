'''
    dfs[1] = 1 + max(dfs[3], dfs[1], dfs[2])
    dp[n] = 1 + max(dp[n - 1], dp[n - 2].....)
'''

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        dp = [-1] * len(nums)
        dp[0] = 0

        for r in range(1, len(nums)):
            for l in range(r):
                if abs(nums[r] - nums[l]) <= target and dp[l] != -1:
                    dp[r] = max(dp[r], 1 + dp[l])
        # print(dp)
        return dp[-1]