class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = cur_sum = float('-inf')
        
        for num in nums:
            cur_sum = max(cur_sum + num, num)
            max_sum = max(max_sum, cur_sum)
            
        return max_sum