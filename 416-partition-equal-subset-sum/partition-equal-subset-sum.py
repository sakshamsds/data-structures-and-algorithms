'''
        0   1   2   3   4   5   6   7   8   9   10  11
0       T   F   F   F   F   F   F   F   F   F   F   F
1       T   T   F   F   F   F   F   F   F   F   F   F
5       T   T   F   F   F   T   T   F   F   F   F   F
11      T   T   F   F   F   T   T   F   F   F   F   T
5       T   T   F   F   F   T   T   F   F   F   F   T

        0   1   2   3   4
0       T   F   F   F   F
1       T   T   F   F   F
2       T   T   T   T   F
5       T   T   T   T   F
'''



class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # can we make target given the nums, variant of coin change, 0/1 knapsack
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2

        dp = [True] + [False] * target
        for num in nums:
            for t in range(target, num - 1, -1):
                dp[t] = dp[t] or dp[t - num]
            if dp[target]:
                return True

        return dp[target]