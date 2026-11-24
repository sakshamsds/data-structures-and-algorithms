class Solution:
    def stoneGameIII(self, stones: list[int]) -> str:
        n = len(stones)
        stones = stones + [0, 0, 0]
        dp = [0] * (n + 3)

        for i in range(n - 1, -1, -1):
            dp[i] = max(
                stones[i] - dp[i + 1],
                stones[i] + stones[i + 1] - dp[i + 2],
                stones[i] + stones[i + 1] + stones[i + 2] - dp[i + 3]
            )
        
        if dp[0] == 0:
            return "Tie"
        if dp[0] > 0:
            return "Alice"
        return "Bob"