class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}

        for num in nums:
            new_dp = collections.defaultdict(int)
            for k, ways in dp.items():
                new_dp[k - num] += ways
                new_dp[k + num] += ways
            dp = new_dp
            
        return dp.get(target, 0)
