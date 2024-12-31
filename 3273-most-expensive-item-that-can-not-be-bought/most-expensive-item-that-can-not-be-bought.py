'''
3, 5
1   2   3   4   5   6   7   8   9   10  11  12  13  14  15
N   N   Y   N   Y   Y   N   Y   Y   Y   Y   Y   Y   Y   Y
0   0   1   0   1   1   0   1   1   1   1   1   1   1   1
'''


class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        dp = [0] * (1 + primeOne * primeTwo)
        dp[primeOne] = 1
        dp[primeTwo] = 1
        most_exp = 1
        for i in range(1, 1 + primeOne * primeTwo):
            if i - primeOne > 0:
                dp[i] |= dp[i - primeOne]
            if i - primeTwo > 0:
                dp[i] |= dp[i - primeTwo]

            if dp[i] == 0:
                most_exp = i

        return most_exp
        
