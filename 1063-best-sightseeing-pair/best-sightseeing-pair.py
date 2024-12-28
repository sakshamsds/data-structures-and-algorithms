class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        i, mx_score = 0, 0

        for j in range(1, len(values)):
            mx_score = max(mx_score, values[i] + i + values[j] - j)
            if values[j] + j > values[i] + i:
                i = j

        return mx_score