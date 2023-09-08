class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        dp = [0, 1]

        res = []
        for i in range(1, numRows + 1):
            new_dp = [0] * (i + 1)
            for j in range(1, i + 1):
                new_dp[j] = dp[j - 1] + dp[j]
            res.append(new_dp[1:])
            dp = new_dp
            dp.append(0)

        return res