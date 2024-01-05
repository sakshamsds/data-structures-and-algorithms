'''
start from last index
1, 2, 4, 3
LIS[3] = 1
LIS[2] = 1 
         or 1 + LIS[3] if nums[2] < nums[3]
LIS[1] = 1 
         or 1 + LIS[2] if nums[1] < nums[2]
         or 1 + LIS[3] if nums[1] < nums[3]
LIS[0] = 1
         or 1 + LIS[1] if nums[0] < nums[1]
         ...

    1   2   4   3
3               1
4           1   1   
2       2   1   1
1   3   2   1   1

    10  9   2   5   4   7   101 18
10  1   
9   1   1
2   1   1   1
5   1   1   1   2
4   1   1   1   2   2
7   1   1   1   2   2   3                    
101 1   1   1   2   2   3   4                        
18  1   1   1   2   2   3   4   4                            
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):   # check all the next numbers
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)