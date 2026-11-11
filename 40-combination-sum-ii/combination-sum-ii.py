class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        comb = []
        candidates.sort()

        def backtrack(i, curSum):
            if curSum == target:
                res.append(comb.copy())
                return
            
            if curSum > target:
                return

            prev = -1
            for j in range(i, len(candidates)):
                if candidates[j] == prev:
                    continue
                comb.append(candidates[j])
                backtrack(j + 1, curSum + candidates[j])
                comb.pop()
                prev = candidates[j]

        backtrack(0, 0)
        return res