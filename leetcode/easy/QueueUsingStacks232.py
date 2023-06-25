from collections import deque

class MyQueue:

    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()

    def push(self, x: int) -> None:
        # from s2 push all in s1
        # add new in s1
        # from s1 push all to s2

        for _ in range(len(self.s2)):
            self.s1.append(self.s2.pop())

        self.s1.append(x)

        for _ in range(len(self.s1)):
            self.s2.append(self.s1.pop())


    def pop(self) -> int:
        return self.s2.pop()

    def peek(self) -> int:
        return self.s2[-1]

    def empty(self) -> bool:
        return len(self.s2) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()