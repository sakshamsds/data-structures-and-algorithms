'''
idx     0   1   2   3   4   5
num     1   2   3   4   6   8
        1   2   2   3   3   4
prev    0   0   0   1   1   3
'''

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [(1, -1)] * len(nums)    # longest, prev
        longest, max_idx = -1, 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i][0] < 1 + dp[j][0]:
                    dp[i] = (1 + dp[j][0], j)
            if dp[i][0] > longest:
                longest = dp[i][0]
                max_idx = i
        # print(dp, i)
        subset = []
        while max_idx != -1:
            subset.append(nums[max_idx])
            max_idx = dp[max_idx][1]
        return subset[::-1]