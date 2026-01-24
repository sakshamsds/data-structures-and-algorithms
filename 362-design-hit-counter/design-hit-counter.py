class HitCounter(object):

    def __init__(self):
        self.ts = []

    def hit(self, timestamp):
        """
        :type timestamp: int
        :rtype: None
        """
        self.ts.append(timestamp)

    def getHits(self, timestamp):
        """
        :type timestamp: int
        :rtype: int
        """
        if not self.ts:
            return 0

        # reject the higher ts
        l, r = 0, len(self.ts)
        while l < r:
            mid = l + (r - l) // 2
            if timestamp < self.ts[mid]:
                r = mid
            else:
                l = mid + 1

        idx = max(0, l - 1)
        cnt_hits = 0
        min_ts = timestamp - 300        # [t - 300, t]
        for i in range(idx, -1, -1):
            if self.ts[i] <= min_ts:
                break
            cnt_hits += 1

        return cnt_hits

        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)