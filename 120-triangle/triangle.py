'''
2   inf inf inf
5   6
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        num_rows = len(triangle)
        dp = [float(inf)] * num_rows
        dp[0] = triangle[0][0]

        for row in range(1, num_rows):
            for i in range(row, 0, -1):
                dp[i] = triangle[row][i] + min(dp[i - 1], dp[i])
            dp[0] = dp[0] + triangle[row][0]
            # print(dp)

        return min(dp)
        
                