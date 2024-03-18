class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        shot_pos = points[0][1]
        shots = 1
        for l, r in points:
            if shot_pos < l:
                shot_pos = r            # need another shot
                shots += 1
        return shots