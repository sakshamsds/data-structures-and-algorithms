class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        num_rows = len(triangle)
        dp = [float('inf')] + [0]

        for r in range(1, num_rows + 1):
            num_cols = len(triangle[r - 1])
            next_dp = [float('inf')] + triangle[r - 1] + [float('inf')]
            # print(dp)
            # print(next_dp)
            for c in range(1, num_cols + 1):
                next_dp[c] += min(dp[c - 1], dp[c])
            dp = next_dp 

        return min(dp[1:])