class DetectSquares:

    def __init__(self):
        self.points = dict()    # pt -> freq

    def add(self, point: list[int]) -> None:
        x, y = point[0], point[1]
        if (x, y) not in self.points:
            self.points[(x, y)] = 0
        self.points[(x, y)] += 1

    def count(self, point: list[int]) -> int:
        # print(self.points)
        squares = 0
        x1, y1 = point[0], point[1]
        for p2, f in self.points.items():
            x2, y2 = p2[0], p2[1]
            if (
                abs(x1 - x2) != abs(y1 - y2) or
                x1 == x2 or y1 == y2 or 
                (x1, y2) not in self.points or 
                (x2, y1) not in self.points
                ):
                continue
            squares += f * self.points[(x1, y2)] * self.points[(x2, y1)]
        return squares


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)