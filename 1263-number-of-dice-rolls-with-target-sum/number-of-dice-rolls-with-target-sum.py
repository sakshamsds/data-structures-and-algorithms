class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # 1 2 3 ... k or target whichever is the min
        # store n, target
        MOD = 1e9 + 7
        cache = {}

        def dfs(n, cur_target):
            if cur_target == 0 or cur_target > (n * k): # target out of range
                return 0

            if n == 1:  # keep rolling until n == 1
                return 1

            if (n, cur_target) in cache:
                return cache[(n, cur_target)]

            ways = 0
            for i in range(1, min(cur_target, k) + 1):  # roll the dice again
                ways += dfs(n - 1, cur_target - i)
            cache[(n, cur_target)] = ways
            return ways

        return dfs(n, target) % (10**9 + 7)
