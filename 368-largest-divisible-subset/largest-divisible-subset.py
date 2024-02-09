class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        self.res, subset = [], []
        cache = {}

        def dfs(largest, idx):
            if (largest, idx) in cache and cache[(largest, idx)] >= len(subset):
                return 
            cache[(largest, idx)] = len(subset)
            
            if idx == len(nums):
                if len(subset) > len(self.res):
                    self.res = subset.copy()
                return len(subset)

            # don't add the current num
            dfs(largest, idx + 1)

            # add cur num if statisfies the condition
            if nums[idx] % largest == 0:
                subset.append(nums[idx])
                dfs(nums[idx], idx + 1)
                subset.pop()
            return 
        
        dfs(1, 0)
        return self.res