'''
1   2   6   9
l   r   
    l   r
'''

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        for r in range(len(nums)):
            if nums[l] * k < nums[r]:
                l += 1

        return l
