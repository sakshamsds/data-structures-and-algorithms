class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        stack = []      # non increasing order
        for i, num in enumerate(nums):
            if not stack or nums[stack[-1]] > num:
                stack.append(i)

        # print(stack)
        maxWidth = 0
        for r in range(len(nums) - 1, -1, -1):
            while stack and nums[r] >= nums[stack[-1]]:
                maxWidth = max(maxWidth, r - stack.pop())

        return maxWidth