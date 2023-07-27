# 
# dp = [0, 0] * 10

import math
dp = [[math.inf, 0] for _ in range(10 + 2)]
dp[0][0] = 0
print(dp)
print(dp[1][0])