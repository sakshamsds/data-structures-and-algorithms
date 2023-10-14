class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt_zeros = 0
        zero_ptr = 0        
    
        for num in nums:
            if num != 0:
                nums[zero_ptr] = num
                zero_ptr += 1
            else:
                cnt_zeros += 1
                
        for i in range(len(nums) - cnt_zeros, len(nums)):
            nums[i] = 0
            