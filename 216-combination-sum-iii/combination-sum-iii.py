class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res = []
        comb = []

        def dfs(digit, curSum):
            # print(digit, curSum, comb)
            if len(comb) == k:
                if curSum == n:
                    res.append(comb.copy())
                return

            if curSum > n or digit == 10:
                return

            # don't pick cur
            dfs(digit + 1, curSum)

            # pick cur
            comb.append(digit)
            dfs(digit + 1, curSum + digit)
            comb.pop()

        dfs(1, 0)
        return res