class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        comb = []

        def dfs(i, curSum):
            if i == len(candidates):
                if curSum == target:
                    res.append(comb.copy())
                return

            if curSum > target:
                return
            
            # skip cur
            dfs(i + 1, curSum)

            comb.append(candidates[i])
            dfs(i, curSum + candidates[i])
            comb.pop()

        dfs(0, 0)
        return res
        