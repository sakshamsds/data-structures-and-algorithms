class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        @cache
        def dfs(i, j):
            if i == len(s):
                if j == len(t):
                    return 1
                else:
                    return 0

            if j == len(t):
                return 1    

            # s rem is less than t rem break
            if len(s) - i < len(t) - j:
                return 0

            # skip cur char in s
            ways = dfs(i + 1, j)

            # pick cur char in s
            if s[i] == t[j]:
                ways += dfs(i + 1, j + 1)

            return ways

        r = dfs(0, 0)
        return r