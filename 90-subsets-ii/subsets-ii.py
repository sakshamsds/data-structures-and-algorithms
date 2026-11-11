class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = set()
        subset = []

        def backtrack(i):
            res.add(tuple(sorted(subset.copy())))
            for j in range(i, len(nums)):
                subset.append(nums[j])
                backtrack(j + 1)
                subset.pop()

        backtrack(0)
        return [list(sub) for sub in res]