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
        for i in range(n):
            arrivalTime.append(dist[i]/speed[i])

        arrivalTime.sort()

        for t in range(n):
            if arrivalTime[t] <= t:
                return t

        return n


