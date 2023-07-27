class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)      # num_rows
        n = len(word2)      # num_cols

        table = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1): table[i][0] = i
        for i in range(n + 1): table[0][i] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                trans_cost = 0 if word1[i - 1] == word2[j - 1] else 1
                table[i][j] = min(table[i][j - 1] + 1,
                                  table[i - 1][j] + 1,
                                  table[i - 1][j - 1] + trans_cost)
                
        return table[-1][-1]
    
# https://www.youtube.com/watch?v=XYi2-LPrwm4
    
print(Solution().minDistance('ros', 'horse'))