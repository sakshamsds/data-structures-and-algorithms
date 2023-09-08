class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = -101
        l = 0 

        for r, num in enumerate(nums):
            if num != prev:   
                nums[l] = num
                l += 1
                prev = num
                
        return l
                
        