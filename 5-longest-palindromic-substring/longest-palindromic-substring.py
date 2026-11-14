class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest, maxL, maxR = 0, 0, 0

        for m in range(n):
            for l, r in [(m, m), (m, m + 1)]:
                while l >= 0 and r < n and s[l] == s[r]:
                    if r - l + 1 > longest:
                        longest, maxL, maxR = r - l + 1, l, r
                    l -= 1
                    r += 1

        return s[maxL:maxR+1]        