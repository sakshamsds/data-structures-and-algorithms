class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i, num in enumerate(nums, 1):
            res ^= num ^ i
        return res

        # n = len(nums)
        # return n * (n + 1) // 2 - sum(nums)