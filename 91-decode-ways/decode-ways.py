class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        cache = {}
        
        def dfs(i):
            if i == n:
                return 1

            if i in cache:
                return cache[i]

            if s[i] == '0':
                return 0

            # use current as single
            num = dfs(i + 1)

            # use current and next
            if i < n - 1 and int(s[i:i+2]) <= 26:
                num += dfs(i + 2)

            cache[i] = num
            return num

        return dfs(0)