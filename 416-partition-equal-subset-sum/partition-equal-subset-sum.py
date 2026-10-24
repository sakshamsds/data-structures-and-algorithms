class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        cache = {}

        total = sum(nums)
        if total & 1 == 1:
            return False
        half = total // 2

        def dfs(i, rem):
            if rem == 0:
                return True
            if i == len(nums):
                return False

            if (i, rem) in cache:
                return cache[(i, rem)]

            cache[(i, rem)] = dfs(i + 1, rem) or dfs(i + 1, rem - nums[i])
            return cache[(i, rem)]

        return dfs(0, half)