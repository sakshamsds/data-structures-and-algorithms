class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        if total % 2 == 1:
            return False

        subset_sum = total // 2

        dp = [True] + [False] * subset_sum

        for num in nums:
            for amt in range(subset_sum, num - 1, -1):
                dp[amt] = dp[amt] or dp[amt - num]
            

        return dp[-1]