class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dp(i, j):
            rob, no_rob = 0, 0
            for k in range(i, j):
                rob, no_rob = no_rob + nums[k], max(rob, no_rob)
            return max(rob, no_rob)

        return max(nums[0], dp(0, len(nums) - 1), dp(1, len(nums)))