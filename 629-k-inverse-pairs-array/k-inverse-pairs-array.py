'''
            k
        0   1   2
    0   1   0   0
n   1   1   0   0
    2   1   1   0
    3   1   2   2

dp[n][k] = number of arrays with k inv pairs, given n elements 
'''

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        # TC - O(n * n * k)
        # SC - O(k)
        MOD = 10 ** 9 + 7
        prev = [0] * (k + 1) 
        prev[0] = 1

        for cur_n in range(1, n + 1):
            cur = [0] * (k + 1)
            total = 0   # sliding window
            for cur_k in range(0, k + 1):
                if cur_k >= cur_n:
                    total -= prev[cur_k - cur_n]
                total = (total + prev[cur_k]) % MOD
                cur[cur_k] = total
            prev = cur

        return prev[k]