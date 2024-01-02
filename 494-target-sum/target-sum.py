class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {(len(nums), target): 1}

        def dfs(i, cur_sum):
            if (i, cur_sum) in cache:       # top down dp
                return cache[(i, cur_sum)]

            if i == len(nums):      # reached end but curSum != target
                return 0
            
            ways = dfs(i + 1, cur_sum + nums[i]) + dfs(i + 1, cur_sum - nums[i])
            cache[(i, cur_sum)] = ways
            return ways

        return dfs(0, 0)