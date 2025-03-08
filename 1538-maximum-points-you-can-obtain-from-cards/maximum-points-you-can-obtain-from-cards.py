class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)

        size = len(cardPoints) - k
        cur_points, min_points = 0, float('inf')
        for i in range(size - 1):
            cur_points += cardPoints[i]

        for i in range(size - 1, len(cardPoints)):
            cur_points += cardPoints[i]
            min_points = min(cur_points, min_points)
            cur_points -= cardPoints[i - size + 1]

        return sum(cardPoints) - min_points