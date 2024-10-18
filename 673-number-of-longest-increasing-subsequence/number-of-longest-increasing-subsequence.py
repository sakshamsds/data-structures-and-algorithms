class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [[1, 1]] * len(nums)    # longest sub len ending at i
        # (size, cnt)

        mx_len, cnt = 1, 1
        for r in range(1, len(nums)):
            for l in range(r):
                if nums[r] > nums[l]:
                    if dp[r][0] == dp[l][0] + 1:
                        dp[r][1] += dp[l][1]
                    elif dp[r][0] < dp[l][0] + 1:
                        dp[r] = [dp[l][0] + 1, dp[l][1]]

            if dp[r][0] == mx_len:
                cnt += dp[r][1]
            elif dp[r][0] > mx_len:
                mx_len, cnt = dp[r]

        # print(dp)
        return cnt
