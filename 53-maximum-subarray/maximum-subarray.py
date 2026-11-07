class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curSum, maxSum = float('-inf'), float('-inf')
        for num in nums:
            curSum = max(curSum, 0) + num
            maxSum = max(maxSum, curSum)
        return maxSum
