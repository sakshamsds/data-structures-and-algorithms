'''
    dir
    1, 0    E
    0,  1   N
    -1, 0   W
    0, -1   S
'''

class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.x, self.y = 0, 0
        self.dir = (1, 0)
        self.dirMap = {
            (1, 0): "East",
            (0, 1): "North",
            (-1, 0): "West",
            (0, -1): "South",
        }
        self.moved = False

    def _keepInBounds(self) -> None:
        if self.x == self.width:
            self.x -= 1
            self.y += 1
            self.dir = (0, 1)
        elif self.y == self.height:
            self.y -= 1
            self.x -= 1
            self.dir = (-1, 0)
        elif self.x == -1:
            self.x = 0
            self.y -= 1
            self.dir = (0, -1)
        elif self.y == -1:
            self.y = 0
            self.x += 1
            self.dir = (1, 0)

    def step(self, num: int) -> None:
        self.moved = True
        num %= 2 * (self.width + self.height - 2)

        if num == 0:
            num = 2 * (self.width + self.height - 2)
        
        for _ in range(num):
            self.x += self.dir[0]
            self.y += self.dir[1]
            self._keepInBounds()

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        if not self.moved:
            return "East"
        return self.dirMap[self.dir]
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()