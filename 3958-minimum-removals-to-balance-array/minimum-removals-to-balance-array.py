'''
1   2   6   9
l   r   
    l   r
'''

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, max_window = 0, 0

        for r in range(len(nums)):
            while nums[l] * k < nums[r]:
                l += 1
            max_window = max(max_window, r - l + 1)

        return len(nums) - max_window
