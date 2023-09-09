class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {0: 1}
        
        def dfs(target_sum):
            if target_sum < 0:
                return 0
            if target_sum in cache:
                return cache[target_sum]
                
            count = 0
            for num in nums:
                count += dfs(target_sum - num)        
            cache[target_sum] = count
            return count

        return dfs(target)

