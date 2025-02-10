'''
-2  1   -3  4   -1  2   1   -5  4
-2  1   -2  4   3   5   6   1   5
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest, cur_sum = float('-inf'), float('-inf')
        for num in nums:
            cur_sum = max(num, num + cur_sum)
            largest = max(largest, cur_sum)
        return largest
