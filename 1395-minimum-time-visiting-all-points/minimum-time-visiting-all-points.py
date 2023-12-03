class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        for i in range(1, len(points)):
            vert_dist = abs(points[i][1] - points[i - 1][1])
            hori_dist = abs(points[i][0] - points[i - 1][0])
            total_time += min(hori_dist, vert_dist) + abs(hori_dist - vert_dist) 

        return total_time