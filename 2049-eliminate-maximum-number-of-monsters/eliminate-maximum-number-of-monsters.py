'''
weapon charged every minute

3, 2, 4
5, 3, 2

1, 1, 2, time taken to arrive
push in heap
'''

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        arrivalTime = []
        for i, (d, s) in enumerate(zip(dist, speed)):
            heapq.heappush(arrivalTime, d/s)
        # print(arrivalTime)

        for t in range(n):
            if heapq.heappop(arrivalTime) <= t:
                return t

        return n


