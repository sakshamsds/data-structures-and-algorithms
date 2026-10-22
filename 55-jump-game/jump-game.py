class Solution:
    def canJump(self, nums: list[int]) -> bool:
        r = 0
        for i, num in enumerate(nums[:-1]):
            if i <= r:
                r = max(r, i + num)
                if r >= len(nums) - 1:  # reach last index
                    return True
        return r >= len(nums) - 1