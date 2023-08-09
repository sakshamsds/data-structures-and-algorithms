from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        no_rob, rob_cur = 0, 0

        for num in nums:
            no_rob, rob_cur = max(no_rob, rob_cur), no_rob + num

        return max(no_rob, rob_cur)
