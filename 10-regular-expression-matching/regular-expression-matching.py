class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(i, j):
            key = (i, j)
            if key in cache:
                return cache[key]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            match = (i < len(s)) and (s[i] == p[j] or p[j] == '.')
            if j + 1 < len(p) and p[j + 1] == '*':      # if the next element is *, use it or don't use it
                cache[key] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return cache[key]

            if match:
                cache[key] = dfs(i + 1, j + 1)
                return cache[key]

            cache[key] = False
            return False

        return dfs(0, 0)