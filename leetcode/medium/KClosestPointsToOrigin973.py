from typing import List

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # easiest solution = sorting, (O(n * log n))
        # sorting not required, use min heap

        # add all in a min heap in O(n)
        # pop k times in O(klogn), which is less than nlogn
        # O(n + klogn)

        min_heap = []
        for x, y in points:
            dist = x**2 + y**2
            min_heap.append([dist, x, y])

        heapq.heapify(min_heap)

        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(min_heap)
            res.append([x, y])
        
        return res
