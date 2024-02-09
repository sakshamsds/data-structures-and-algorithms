'''
    10  9   2   5   3   7   101 18
10  1   1   1   2   2   3   4    4

ending with num, what is the longest common subsequence
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
        