'''
0 1
0 1 
0 1 1 
0 1 2 1 
0 1 3 3 1 
0 1 4 6 4 1 


'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        dp = [0, 1]
        for r in range(numRows):
            next_dp = [0] * (r + 1)
            for i in range(1, r + 1):
                next_dp[i] = dp[i] + dp[i - 1]
            next_dp.append(1)
            res.append(next_dp[1:])
            dp = next_dp
            
        return res