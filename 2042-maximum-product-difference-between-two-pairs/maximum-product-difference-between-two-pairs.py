class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        a, b, c, d = nums[-1], nums[-2], nums[0], nums[1]
        return a * b - c * d