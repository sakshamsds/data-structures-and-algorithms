'''
    2   0   2   1   1   0
    0   0   1   1   2   2


    1   0   0   2   0  1   1
    l           m   m      r
'''

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, m, r = 0, 0, len(nums) - 1

        while m <= r:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1
            elif nums[m] == 2:
                nums[m], nums[r] = nums[r], nums[m]
                r -= 1
            else:
                m += 1

        