class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:
        uniques = set(map(tuple, points))
        # print(uniques)
        minArea = float('inf')
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1x, p1y = points[i]
                p2x, p2y = points[j]
                if p1x == p2x or p1y == p2y or (p2x, p1y) not in uniques or (p1x, p2y) not in uniques:
                    continue
                # print(p1x, p1y, p2x, p2y, abs(p1y - p2y) * abs(p1x - p2x))
                minArea = min(minArea, abs(p1y - p2y) * abs(p1x - p2x))

        return 0 if minArea == float('inf') else minArea