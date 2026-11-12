class MedianFinder:

    def __init__(self):
        self.lower = []          # max heap, can contain the extra element
        self.upper = []         # min heap

    def addNum(self, num: int) -> None:
        if not self.lower or -self.lower[0] >= num:
            heapq.heappush(self.lower, -num)
        else:
            heapq.heappush(self.upper, num)


        # adjust the sizes
        if len(self.upper) > len(self.lower):
            heapq.heappush(self.lower, -heapq.heappop(self.upper))

        if len(self.lower) - len(self.upper) == 2:
            heapq.heappush(self.upper, -heapq.heappop(self.lower))


    def findMedian(self) -> float:
        if len(self.lower) == len(self.upper):
            return (self.upper[0] - self.lower[0]) / 2 
        else:
            return -self.lower[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()