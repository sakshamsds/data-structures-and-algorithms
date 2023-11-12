class Solution:
    def longestPalindrome(self, s: str) -> str:
        # check substring for every starting from every possible idx

        res_l, res_r = 0, 0
        max_size = 0
        for i in range(len(s)):
            # one odd length
            # one even length
            for l, r in [(i, i), (i, i + 1)]:
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if r - l + 1 > max_size:
                        max_size = r - l + 1
                        res_l = l
                        res_r = r
                    l -= 1
                    r += 1

        return s[res_l:res_r + 1]