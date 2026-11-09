class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        MAX = len(nums)
        for i, num in enumerate(nums):
            if num < 1:
                nums[i] = MAX + 1
        # print(nums)

        for i in range(MAX):
            idx = abs(nums[i]) - 1
            if idx < MAX:
                nums[idx] = -abs(nums[idx])
                # print(idx, nums[idx])

        # print(nums)
        for i in range(MAX):
            if nums[i] > 0:
                return i + 1
        return MAX + 1