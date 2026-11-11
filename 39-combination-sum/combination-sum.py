class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []
        comb = []

        def backtrack(i, curSum):
            if curSum == target:
                res.append(comb.copy())

            if curSum > target:
                return
            
            for j in range(i, len(nums)):
                comb.append(nums[j])
                backtrack(j, curSum + nums[j])
                comb.pop()

        backtrack(0, 0)
        return res
        