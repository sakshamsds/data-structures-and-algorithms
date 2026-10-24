class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = {0: -1}       # more_ones, i
        more_ones = 0
        mx_size = 0
        for i, num in enumerate(nums):
            if num == 1:
                more_ones += 1
            else:
                more_ones -= 1
            if more_ones in seen:
                mx_size = max(mx_size, i - seen[more_ones])
            else:
                seen[more_ones] = i
        return mx_size