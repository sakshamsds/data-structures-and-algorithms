'''
11106 -> 1 -> 1106 -> 1 -> 106 -> 1 -> 06
                               -> 10 -> 6
                   -> 11 -> 06
      -> 11 -> 106
'''


class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {len(s): 1}

        def dfs(i):
            if i in cache:
                return cache[i]

            if s[i] == '0':
                return 0

            # take 1 char
            ways = dfs(i + 1)

            # take 2 char
            if i + 2 <= len(s) and ('1' <= s[i:i + 2] <= '26'):
                ways += dfs(i + 2)

            cache[i] = ways
            return ways

        return dfs(0)