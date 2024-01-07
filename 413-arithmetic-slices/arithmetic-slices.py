class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        prev_diff = -inf
        size = -1
        res = 0

        for i in range(1, len(nums)):
            cur_diff = nums[i] - nums[i - 1]
            if cur_diff == prev_diff:
                size += 1
                if size > 2:
                    res += size - 2
            else:
                prev_diff = cur_diff
                size = 2

        return res