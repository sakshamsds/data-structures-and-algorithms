class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        maxSum, curSumPos = nums[0], 0
        minSum, curSumNeg = nums[0], 0
        total = 0
        for num in nums:   
            curSumPos = max(curSumPos, 0) + num     # discard neg
            maxSum = max(maxSum, curSumPos)
            curSumNeg = min(curSumNeg, 0) + num     # discard pos
            minSum = min(minSum, curSumNeg)
            total += num

        if total == minSum: # all neg
            return maxSum

        return max(maxSum, total - minSum)