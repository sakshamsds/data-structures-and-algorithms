import heapq
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        # O(n)
        num_pass = [0] * 1001

        for trip in trips:
            p, start, end = trip
            num_pass[start] += p
            num_pass[end] -= p

        cur_pass = 0
        for i in range(1001):
            cur_pass += num_pass[i]
            if cur_pass > capacity:
                return False

        return True

        # # O(nlogn)
        # trips.sort(key = lambda x : x[1], reverse=False)
        # min_heap = []       # [end, passengers] pair
        # cur_pass = 0
        # for trip in trips:
        #     num_pass, start, end = trip

        #     while min_heap and min_heap[0][0] <= start:
        #         cur_pass -= min_heap[0][1]      # pop the passengers
        #         heapq.heappop(min_heap)

        #     cur_pass += num_pass
        #     heapq.heappush(min_heap, [end, num_pass])

        #     if cur_pass > capacity:
        #         return False

        # return True

        # # O(n^2)
        # num_passengers = [0] * 1001

        # for trip in trips:
        #     for i in range(trip[1], trip[2]):
        #         num_passengers[i] += trip[0]
        #     # num_passengers[trip[1]] += trip[0]
        #     # num_passengers[trip[2]] -= trip[0]
        
        # # print(num_passengers)
        # for x in num_passengers:
        #     if x > capacity:
        #         return False

        # return True
