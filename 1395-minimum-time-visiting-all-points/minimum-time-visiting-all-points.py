class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        for i in range(1, len(points)):
            cur_x, cur_y = points[i - 1]
            target_x, target_y = points[i]
            total_time += max(abs(cur_x - target_x), abs(cur_y - target_y))

        return total_time