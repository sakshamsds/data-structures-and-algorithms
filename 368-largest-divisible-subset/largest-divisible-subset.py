'''
    0       1       2       3       4       5
    2       8       14      16      21      28
    3,1     2,3     2,5     1,-1    1,-1    1,-1
'''

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        dp = [[1, -1] for _ in range(n)]
        longest_size, longest_i = 1, 0
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[j] % nums[i] == 0 and dp[i][0] < 1 + dp[j][0]:
                    dp[i][0] = 1 + dp[j][0]
                    dp[i][1] = j
            if dp[i][0] > longest_size:
                longest_size = dp[i][0]
                longest_i = i
        # print(dp, longest_size, longest_i)

        longest = []
        for _ in range(longest_size):
            longest.append(nums[longest_i])
            longest_i = dp[longest_i][1]
        
        return longest