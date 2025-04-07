'''
        1   5   11  5
'''

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        cache = {}

        def dfs(i, rem):
            if rem == 0:
                return True

            if i == len(nums):
                return False

            key = (i, rem)
            if key in cache:
                return cache[key]

            cache[key] = dfs(i + 1, rem) or dfs(i + 1, rem - nums[i])
            return cache[key]

        return dfs(0, total // 2)