class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {len(s): 1}

        def dfs(i):
            if i in cache:
                return cache[i]

            cur_count = 0
            if s[i] != '0':     # checking single digit
                cur_count += dfs(i + 1)
            
            if i + 1 < len(s) and '1' <= s[i:i + 2] <= '26':    # check two digits
                cur_count += dfs(i + 2)
            cache[i] = cur_count
            return cur_count
        
        return dfs(0)