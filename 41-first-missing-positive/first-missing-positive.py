class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # num < 1 and > len(nums) doesn't matter
        # use the concept of index marking

        n = len(nums)
        for i, num in enumerate(nums):
            if num < 1:
                nums[i] = n + 1

        for num in nums:
            idx = abs(num) - 1
            if idx < n and nums[idx] > 0:
                nums[idx] = -nums[idx]

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1