class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        subset = []
        nums.sort()

        def backtrack(i):
            res.append(subset.copy())
            prev = -11
            for j in range(i, len(nums)):
                if nums[j] == prev:
                    continue
                subset.append(nums[j])
                backtrack(j + 1)
                subset.pop()
                prev = nums[j]

        backtrack(0)
        return res