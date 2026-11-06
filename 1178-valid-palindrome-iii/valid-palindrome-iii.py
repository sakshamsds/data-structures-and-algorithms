class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # find longest palindromic subsequence
        # LPS + k >= len(s)

        def lcs(s1, s2):
            m, n = len(s1), len(s2)
            prev_dp = [0] * (n + 1)
            for r in range(m):
                new_dp = [0] * (n + 1)
                for c in range(n):
                    if s1[r] == s2[c]:
                        new_dp[c + 1] = 1 + prev_dp[c]
                    else:
                        new_dp[c + 1] = max(prev_dp[c + 1], new_dp[c])
                prev_dp = new_dp
            return prev_dp[-1]

        def lps(s):
            return lcs(s, s[::-1])

        return lps(s) + k >= len(s)