class Solution:
    def countSubstrings(self, s: str) -> int:
        # start from the center
        # account for even and odd len strings
        res = 0

        for i in range(len(s)):
            for l, r in [(i, i), (i, i + 1)]:
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1
                res += (r - l) // 2

        return res
