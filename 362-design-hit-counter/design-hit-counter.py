class HitCounter(object):

    def __init__(self):
        self.q = collections.deque()

    def remove(self, ts):
        while self.q and ts - self.q[0] >= 300:
            self.q.popleft()

    def hit(self, timestamp):
        """
        :type timestamp: int
        :rtype: None
        """
        self.remove(timestamp)
        self.q.append(timestamp)

    def getHits(self, timestamp):
        """
        :type timestamp: int
        :rtype: int
        """
        self.remove(timestamp)
        return len(self.q)        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)