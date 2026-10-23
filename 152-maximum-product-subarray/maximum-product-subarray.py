'''
    2   3   -2      4           -2
    2   6   -2      4           96
    2   3   -12     -48         48
'''

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # store min and max pdt at every index
        max_pdt = nums[0]
        cur_max, cur_min = nums[0], nums[0]
        for num in nums[1:]:
            cur_max, cur_min = num * max(1, cur_max, cur_min), num * min(1, cur_max, cur_min )
            max_pdt = max(max_pdt, cur_max, cur_min)
        return max_pdt
