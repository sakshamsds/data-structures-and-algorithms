class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        def getMaxSum(arr):
            cur_sum, max_sum = float(-inf), float(-inf)
            for num in arr:
                cur_sum = max(cur_sum + num, num)
                max_sum = max(cur_sum, max_sum)
            return max_sum

        return max(getMaxSum(nums), getMaxSum([-x for x in nums]))