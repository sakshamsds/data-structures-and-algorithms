'''
2   3   5   2 
'''

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if (
                nums[i] == nums[i - 1] or \
                nums[i] == nums[i - 2] or \
                nums[i] == nums[i - 3]
             ):
                return nums[i]

        return -1
