class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        largest, idx = nums[0], 0
        for i, num in enumerate(nums):
            if num > largest:
                largest, idx = num, i

        n = len(nums)
        res = [0] * n
        res[idx] = -1
        stack = [largest]
        for _ in range(n):
            idx -= 1
            if idx == -1:
                idx = n - 1
            while stack and stack[-1] <= nums[idx]:
                stack.pop()
            res[idx] = stack[-1] if stack else -1
            stack.append(nums[idx])
        return res