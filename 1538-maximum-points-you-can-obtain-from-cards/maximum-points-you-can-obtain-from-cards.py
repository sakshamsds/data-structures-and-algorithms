class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)

        window_size = len(cardPoints) - k
        cur_points = sum(cardPoints[:window_size])
        min_window_sum = cur_points

        for i in range(window_size, len(cardPoints)):
            cur_points += cardPoints[i] - cardPoints[i - window_size]
            min_window_sum = min(cur_points, min_window_sum)

        return sum(cardPoints) - min_window_sum