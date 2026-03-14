'''
    (1, 1, 1), (1, 1, 1), (2, 2, 1) -   4
    (3, 1, 2), (1, 1, 1), (2, 2, 1) -   3
    (3, 1, 2), (3, 1, 2), (2, 2, 1) -   2
    (3, 1, 2), (3, 1, 2), (6, 2, 2) -   1
    (3, 1, 2), (3, 1, 2), (6, 2, 2) -   0
'''

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        # which worker is gonna cut my next height
        pq = []
        for wt in workerTimes:
            pq.append((wt, wt, 1))
        heapq.heapify(pq)

        for _ in range(mountainHeight):
            nxtTime, workerTime, factor = heapq.heappop(pq)
            factor += 1
            heapq.heappush(pq, (nxtTime + workerTime * factor, workerTime, factor))

        return nxtTime



