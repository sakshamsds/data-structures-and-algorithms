'''
1   2   3   4   5   6

1   1   2   2   3   3
'''

class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = 0

        for i in range(len(nums) - 2, len(nums)//3 - 1, -2):
            max_sum += nums[i]

        return max_sum