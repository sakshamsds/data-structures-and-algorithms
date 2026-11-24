class Solution:
    def minAreaFreeRect(self, points: list[list[int]]) -> float:
        # given 3 points
        # p1, p2, p3 -> find p4 in the set

        uniques = set()
        for x, y in points:
            uniques.add((x, y))
        minArea = float('inf')
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                for k in range(j + 1, len(points)):
                    x3, y3 = points[k]

                    if (y2 - y1)  * (y3 - y1) != -(x2 - x1) * (x3 - x1):\
                        continue
                    # print(x1, y1, x2, y2, x3, y3)
                    # oppositie sides of the rectangle or parallelogram are same vectors
                    # D - C = B - A => D = B + C - A
                    # x4 = x2 + x3 - x1, y4 = y2 + y3 - y1
                    x4, y4 = x2 + x3 - x1, y2 + y3 - y1
                    if (x4, y4) not in uniques:
                        continue
                    W = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                    H = math.sqrt((x4 - x2) ** 2 + (y4 - y2) ** 2)
                    minArea = min(minArea, W * H)

        return minArea if minArea != float('inf') else 0