class HitCounter(object):

    def __init__(self):
        self.q = collections.deque()
        self.hits = 0

    def remove(self, ts):
        while self.q and ts - self.q[0][0] >= 300:
            _, hits = self.q.popleft()
            self.hits -= hits

    def hit(self, timestamp):
        """
        :type timestamp: int
        :rtype: None
        """
        self.remove(timestamp)
        hits = 0
        if self.q and self.q[-1][0] == timestamp:
            _, hits = self.q.pop()
            self.hits -= hits
        self.q.append((timestamp, hits + 1))
        self.hits += hits + 1

    def getHits(self, timestamp):
        """
        :type timestamp: int
        :rtype: int
        """
        self.remove(timestamp)
        return self.hits

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)