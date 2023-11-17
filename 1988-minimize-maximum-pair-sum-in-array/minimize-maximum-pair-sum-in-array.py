'''
2, 3, 4, 4, 5, 6
8, 8, 8
'''

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = -1
        for i in range(len(nums)//2):
            max_sum = max(nums[i] + nums[len(nums) - 1 - i], max_sum)
        return max_sum