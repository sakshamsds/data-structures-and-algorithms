class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best_left = values[0] - 1   # best value spot to the left
        best_score = 0

        for i in range(1, len(values)):
            best_score = max(best_score, best_left + values[i])
            best_left = max(best_left, values[i]) - 1

        return best_score
