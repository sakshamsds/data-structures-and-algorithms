class Solution:
    def numSquares(self, n: int) -> int:
        cache = {0: 0}

        def dfs(rem):
            if rem in cache:
                return cache[rem]
            min_sqrs = float('inf')
            for num in range(1, rem + 1):
                sqr = num * num
                if sqr > n:
                    break
                min_sqrs = min(min_sqrs, 1 + dfs(rem - sqr))
            cache[rem] = min_sqrs
            return min_sqrs

        return dfs(n)