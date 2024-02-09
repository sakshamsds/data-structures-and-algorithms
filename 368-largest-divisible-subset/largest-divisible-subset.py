'''
idx     0   1   2   3   4   5
num     1   2   3   4   6   8
        1   2   2   3   3   4
prev    0   0   0   1   1   3
'''

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = []    # longest, prev
        for i in range(len(nums)):
            dp.append((1, i))

        longest, max_idx = -1, 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i][0] < 1 + dp[j][0]:
                    dp[i] = (1 + dp[j][0], j)
            if dp[i][0] > longest:
                longest = dp[i][0]
                max_idx = i

        # print(dp, i)

        # build subset
        cur, prev = max_idx, dp[max_idx][1]
        subset = [nums[cur]]
        while cur != prev:
            cur, prev = prev, dp[prev][1]
            subset.append(nums[cur])
        return subset[::-1]