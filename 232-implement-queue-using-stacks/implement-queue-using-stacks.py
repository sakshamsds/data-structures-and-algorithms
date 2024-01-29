class MyQueue:

    def __init__(self):
        self.s2 = []

    def push(self, x: int) -> None: 
        temp_stack = []   
        while self.s2:
            temp_stack.append(self.s2.pop())
        temp_stack.append(x)
        while temp_stack:
            self.s2.append(temp_stack.pop())

    def pop(self) -> int:
        return self.s2.pop()

    def peek(self) -> int:
        return self.s2[-1]      # equivalent to stack.peek()

    def empty(self) -> bool:
        return not self.s2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()