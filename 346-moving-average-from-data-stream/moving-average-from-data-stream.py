class MovingAverage:

    def __init__(self, size: int):
        self.window = deque([])
        self.maxSize = size
        self.curSum = 0
        self.curSize = 0

    def next(self, val: int) -> float:
        self.window.append(val)
        self.curSize += 1
        self.curSum += val

        if self.curSize > self.maxSize:
            self.curSum -= self.window.popleft()
            self.curSize -= 1

        return self.curSum / self.curSize



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)