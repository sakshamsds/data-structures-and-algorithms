from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # use the hint
        return max(nums[0], 
                    self.house_robber(nums[1:]), 
                    self.house_robber(nums[:-1]))

    def house_robber(self, nums):
        rob, no_rob = 0, 0
        for num in nums:
            rob, no_rob = no_rob + num, max(rob, no_rob)

        return max(rob, no_rob)