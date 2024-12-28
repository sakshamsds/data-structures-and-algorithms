'''
            0   1   2   3   4
            8   1   5   2   6
v[i] + i    8   2   7   5   10
best left   8   8   8   8   10

v[j] - j    8   0   3   -1  2
'''

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best_left, mx_score = -1, -1e5
        for j in range(1, len(values)):
            best_left = max(best_left, values[j - 1] + j - 1)
            mx_score = max(mx_score, best_left + values[j] - j)
        return mx_score