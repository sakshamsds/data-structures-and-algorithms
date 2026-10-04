class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(i, j):
            if (i, j) not in cache:
                if j == len(p):
                    ans = i == len(s)
                else:
                    match = (i < len(s)) and (s[i] == p[j] or p[j] == '.')
                    if j + 1 < len(p) and p[j + 1] == '*':      # if the next element is *, use it or don't use it
                        ans = dfs(i, j + 2) or (match and dfs(i + 1, j))
                    else:
                        ans = match and dfs(i + 1, j + 1)
                cache[(i, j)] = ans
            return cache[(i, j)]

        return dfs(0, 0)