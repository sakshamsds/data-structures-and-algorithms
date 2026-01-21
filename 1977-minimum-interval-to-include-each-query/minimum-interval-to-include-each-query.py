class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort both intervals and queries
        intervals.sort(key=lambda x:x)

        min_heap = []       # size, end
        res = {}
        k = 0
        for q in sorted(queries):
            while k < len(intervals) and intervals[k][0] <= q:
                # print(k)
                heapq.heappush(
                    min_heap, 
                    (intervals[k][1] - intervals[k][0] + 1, intervals[k][1])
                )
                k += 1

            # print(q, i, min_heap)
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            res[q] = min_heap[0][0] if min_heap else -1

        return [res[q] for q in queries]

