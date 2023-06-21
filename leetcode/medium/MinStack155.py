class MinStack:

    def __init__(self):
        self.og_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.og_stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)
        
    def pop(self) -> None:
        self.og_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.og_stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()