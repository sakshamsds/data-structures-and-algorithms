# editorial

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for c in s:
            cur = ord(c) - ord('a')
            mx = 0
            for prev in range(26):
                if abs(cur - prev) <= k:
                    mx = max(mx, 1 + dp[prev])
                
            dp[cur] = max(dp[cur], mx)
        return max(dp)
            