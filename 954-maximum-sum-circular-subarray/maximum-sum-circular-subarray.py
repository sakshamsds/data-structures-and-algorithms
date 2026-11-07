class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        # delete min subarray sum from the total
        max_num = max(nums)
        if max_num <= 0:
            return max_num

        maxSum, curSumPos = float('-inf'), float('-inf')
        minSum, curSumNeg = float('inf'), float('inf')
        total = 0
        for num in nums:   
            curSumPos = max(curSumPos, 0) + num     # discard neg
            maxSum = max(maxSum, curSumPos)
            curSumNeg = min(curSumNeg, 0) + num     # discard pos
            minSum = min(minSum, curSumNeg)
            total += num

        return max(maxSum, total - minSum)