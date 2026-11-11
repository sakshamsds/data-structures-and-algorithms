class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        subset = []

        def backtrack(i):
            res.append(subset.copy())                

            for j in range(i, len(nums)):
                subset.append(nums[j])
                backtrack(j + 1)
                subset.pop()

        backtrack(0)
        return res