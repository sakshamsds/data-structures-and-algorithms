class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left_sum, right_sum = 0, sum(nums)
        
        num_valid_splits = 0
        for i in range(0, len(nums) - 1):
            left_sum += nums[i]
            right_sum -= nums[i]
            if left_sum >= right_sum:
                num_valid_splits += 1
            
        return num_valid_splits
