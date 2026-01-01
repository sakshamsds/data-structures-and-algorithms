'''
if we send anything to upper, we bring the min to lower 
    this way we lower will always be >= upper size
'''

class MedianFinder:

    def __init__(self):
        self.upper = [10 ** 5 + 1]     # min_heap
        self.lower = [10 ** 5 + 1]     # max_heap, negative of lowest

    def addNum(self, num: int) -> None:
        upper_min = self.upper[0]
        if num > upper_min:
            heapq.heappop(self.upper)
            heapq.heappush(self.upper, num)
            heapq.heappush(self.lower, -upper_min)
        else:
            heapq.heappush(self.lower, -num)

        if len(self.lower) == len(self.upper) + 2:
            lower_max = -heapq.heappop(self.lower)
            heapq.heappush(self.upper, lower_max)


    def findMedian(self) -> float:
        if len(self.upper) == len(self.lower):
            return (self.upper[0] + -self.lower[0]) / 2
        else:       # size of lower - upper = 1
            return -self.lower[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()