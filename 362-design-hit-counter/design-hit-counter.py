class HitCounter:

    def __init__(self):
        self.q = deque()        # ts, hits
        self.hits = 0

    def _remove(self, timestamp):
        while self.q and timestamp - self.q[0][0] >= 300:
            self.hits -= self.q.popleft()[1]

    def hit(self, timestamp: int) -> None:
        self._remove(timestamp)
        hits = 0
        if self.q and self.q[-1][0] == timestamp:
            hits = self.q.pop()[1]
        hits += 1
        self.q.append((timestamp, hits))
        self.hits += 1

    def getHits(self, timestamp: int) -> int:
        self._remove(timestamp)
        return self.hits


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)