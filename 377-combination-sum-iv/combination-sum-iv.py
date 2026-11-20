class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = {}

        def dfs(rem):
            if rem == 0:
                return 1
            if rem < 0:
                return 0

            if rem in dp:
                return dp[rem]

            ways = 0
            for num in nums:
                ways += dfs(rem - num)

            dp[rem] = ways
            return ways

        return dfs(target)