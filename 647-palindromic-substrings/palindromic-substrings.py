class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        for m in range(n):
            for l, r in [(m, m), (m, m + 1)]:
                while l >= 0 and r < n and s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
            # print(m, res)
        return res