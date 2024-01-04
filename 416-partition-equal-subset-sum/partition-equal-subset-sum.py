'''
lSum, rSum, idx
lSum, rSum = total - left, idx
lSum, idx
'''

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False

        target_sum = total_sum // 2
        cache = {}

        def dfs(idx, l_sum):
            if idx == len(nums):
                return l_sum == target_sum

            if l_sum > target_sum:        # stop if lSum goes over target
                return False

            if (idx, l_sum) in cache:
                return cache[(idx, l_sum)]
                
            cache[(idx, l_sum)] = dfs(idx + 1, l_sum) or \
                                  dfs(idx + 1, l_sum + nums[idx])
            return cache[(idx, l_sum)]

        return dfs(0, 0)