class MinStack:

    def __init__(self):
        self.stack = []     # value, minValue

    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append((value, value))
        else:
            smaller = min(self.stack[-1][1], value)
            self.stack.append((value, smaller))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()