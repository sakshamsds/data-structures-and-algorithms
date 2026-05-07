class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        # 0-1 knapsack
        dp = [0] * (budget + 1)
        for p, f in zip(present, future):
            for b in range(budget, p - 1, -1):
                dp[b] = max(dp[b], dp[b - p] + f - p)
            # print(dp)

        return dp[-1]