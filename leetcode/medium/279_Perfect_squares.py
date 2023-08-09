class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1
        # print(squares)

        # bottom up dp
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            min_val = float('+inf')
            for square in squares:
                if square <= i:
                    min_val = min(min_val, 1 + dp[i - square])
                else:
                    break
            dp[i] = min_val

        # print(dp)
        return dp[-1]

# TC = O(n * sqrt(n))