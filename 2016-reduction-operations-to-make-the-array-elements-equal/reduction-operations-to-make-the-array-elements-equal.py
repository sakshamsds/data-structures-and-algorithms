class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        num_distinct, res = 0, 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:      # distinct number found
                num_distinct += 1         # gotta reduce the cur num to this level
            res += num_distinct

        return res
            