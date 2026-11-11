class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        subset = []

        # select current number or not
        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return

            # don't choose current
            dfs(i + 1)

            # choose current
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()

        dfs(0)
        return res