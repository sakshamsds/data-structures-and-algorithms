class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        overall_min = idx_min = float('inf')
        overall_max = idx_max = float('-inf')     # ending at that index
        for num in nums:
            idx_max = max(idx_max + num, num)
            overall_max = max(overall_max, idx_max)
            idx_min = min(idx_min + num, num)
            overall_min = min(overall_min, idx_min)
        total = sum(nums)
        if overall_min == total:
            return overall_max

        return max(overall_max, sum(nums) - overall_min)
