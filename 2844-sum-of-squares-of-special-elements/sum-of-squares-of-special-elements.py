class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        res, n = 0, len(nums)
        for i, num in enumerate(nums):
            if n % (i + 1) == 0:
                res += num ** 2
        return res