class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        # use each point as potential right of the bowl
        stack = []  # store left in stack, monotonically decreasing
        bowls = 0

        for r, num in enumerate(nums):
            while stack and nums[stack[-1]] <= num:
                l = stack.pop()
                if r - l + 1 >= 3:
                    bowls += 1
            if stack and r - stack[-1] + 1 >= 3:
                bowls += 1
            stack.append(r)

        return bowls
