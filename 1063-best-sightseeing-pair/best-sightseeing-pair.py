'''
            0   1   2   3   4
            8   1   5   2   6
v[i] + i    8   2   7   5   10

v[j] - j    8   0   3   -1  2
mx          8   3   3   2   2

'''

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        suffix = [v - j for j, v in enumerate(values)]

        for j in range(len(suffix) - 2, -1, -1):
            suffix[j] = max(suffix[j + 1], suffix[j])
        
        mx_score = -1e5
        for i in range(0, len(values) - 1):
            mx_score = max(mx_score, values[i] + i + suffix[i + 1])

        return mx_score