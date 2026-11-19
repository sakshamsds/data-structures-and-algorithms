class FreqStack:

    def __init__(self):
        self.freqs = {}
        self.maxHeap = []       # -f, -order, val
        self.insertionOrder = 0

    def push(self, val: int) -> None:
        self.freqs[val] = self.freqs.get(val, 0) + 1
        heapq.heappush(self.maxHeap, (-self.freqs[val], -self.insertionOrder, val))
        self.insertionOrder += 1

    def pop(self) -> int:
        _, _, val = heapq.heappop(self.maxHeap)
        self.freqs[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()