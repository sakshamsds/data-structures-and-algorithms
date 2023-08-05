from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algorithm
        best_sum = float('-inf')
        current_sum = float('-inf')
        for num in nums:
            current_sum = max(current_sum + num, num)
            best_sum = max(best_sum, current_sum)

        return best_sum

    # def maxSubArray(self, nums):
		# dp = [0]*len(nums)
        # for i,num in enumerate(nums):            
            # dp[i] = max(dp[i-1] + num, num)
        # return max(dp)
