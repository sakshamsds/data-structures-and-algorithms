class Solution:
    def numSquares(self, n: int) -> int:
        # O(n * sqrt(n))
        dp = [0] + [float('inf')] * n
        for num in range(1, n + 1):
            for i in range(1, num + 1):
                if i * i > num:
                    break
                dp[num] = min(dp[num], dp[num - i * i] + 1)
        return dp[-1]