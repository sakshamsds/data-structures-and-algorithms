'''
    2   20  30  40   100     104
'''

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        max_sum = 0
        nums.sort(key=lambda x : x)
        n = len(nums)
        for i in range(n//2):
            max_sum = max(max_sum, nums[i] + nums[n - i - 1])

        return max_sum
