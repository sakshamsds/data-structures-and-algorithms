class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res = []
        comb = []

        def backtrack(i, curSum):
            if len(comb) == k:
                if curSum == n:
                    res.append(comb.copy())
                return
            
            if curSum > n:
                return

            for j in range(i + 1, 10):
                comb.append(j)
                backtrack(j, curSum + j)
                comb.pop()

        backtrack(0, 0)
        return res