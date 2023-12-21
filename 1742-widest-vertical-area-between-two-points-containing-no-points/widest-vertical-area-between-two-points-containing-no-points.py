class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        max_diff = -1
        for i in range(len(points) - 1):
            diff = points[i + 1][0] - points[i][0]
            max_diff = max(diff, max_diff)
        return max_diff

