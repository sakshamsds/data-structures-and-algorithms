class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if m < n:
            return -1

        MOD = 1_000_000_033
        # MOD = 113
        BASE = 26     
        MAX_WEIGHT = 1

        for _ in range(n - 1):
            MAX_WEIGHT = (MAX_WEIGHT * BASE) % MOD   

        def hash(s):
            h = 0
            for c in s:
                h = (h * BASE + ord(c) - ord('a')) % MOD
            return h

        needle_hash = hash(needle)
        window_hash = hash(haystack[:n])

        for l in range(m - n + 1):
            if window_hash == needle_hash and haystack[l:l + n] == needle:
                return l

            if l < m - n:
                first_char_val = ord(haystack[l]) - ord('a')
                last_char_val = ord(haystack[l + n]) - ord('a')
                window_hash = (window_hash - first_char_val * MAX_WEIGHT) % MOD
                window_hash = (window_hash * BASE + last_char_val) % MOD

        return -1
