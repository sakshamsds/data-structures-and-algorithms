class MaxStack:

    def __init__(self):
        self.stack = []     # (x, uid)
        self.maxHeap = []     # (-x, -uid)    # newest UID should come first
        self.removed = set()
        self.uid = 0

    def push(self, x: int) -> None:
        self.stack.append((x, self.uid))
        heapq.heappush(self.maxHeap, (-x, -self.uid))
        self.uid += 1

    def _stackDeletion(self) -> None:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()

    def pop(self) -> int:
        self._stackDeletion()
        x, uid = self.stack.pop()
        self.removed.add(uid)
        return x

    def top(self) -> int:
        self._stackDeletion()
        return self.stack[-1][0]

    def _heapDeletions(self) -> None:
        while self.maxHeap and -self.maxHeap[0][1] in self.removed:
            heapq.heappop(self.maxHeap)

    def popMax(self) -> int:
        self._heapDeletions()
        x, uid = heapq.heappop(self.maxHeap)
        self.removed.add(-uid)
        return -x

    def peekMax(self) -> int:
        self._heapDeletions()
        return -self.maxHeap[0][0]

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()