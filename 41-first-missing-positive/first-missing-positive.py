class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # remove negatives
        for i, num in enumerate(nums):
            if num < 1:
                nums[i] = len(nums) + 5

        # index marking
        for i, num in enumerate(nums):
            idx = abs(num) - 1
            if idx < len(nums):
                nums[idx] = -abs(nums[idx])

        # find first missing
        for i, num in enumerate(nums):
            if num > 0:
                return i + 1

        return len(nums) + 1

        