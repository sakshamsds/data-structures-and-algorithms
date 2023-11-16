'''
11106 -> 1 -> 1106 -> 1 -> 106 -> 1 -> 06
                               -> 10 -> 6
                   -> 11 -> 06
      -> 11 -> 106
'''


class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dfs(i):
            if i >= len(s):
                return 1

            if s[i] == '0':
                return 0

            ways = 0
            # take 1 char
            if s[i] != '0':
                ways += dfs(i + 1)

            # take 2 char
            if i + 2 <= len(s) and ('1' <= s[i:i + 2] <= '26'):
                ways += dfs(i + 2)

            return ways

        return dfs(0)