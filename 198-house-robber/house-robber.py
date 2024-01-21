class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        for num in nums:
            curr, prev = prev + num, max(prev, curr)
        return max(prev, curr)