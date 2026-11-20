class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        intervals.sort(key=lambda x:x[0])
        sortedQueries = sorted([(query, idx) for idx, query in enumerate(queries)])

        minHeap = []        # size, end
        res = [-1] * len(queries)
        i = 0
        for query, queryIdx in sortedQueries:
            # add to heap
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]
                heapq.heappush(minHeap, (end - start + 1, end))
                i += 1

            # remove from heap
            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)

            if minHeap:
                res[queryIdx] = minHeap[0][0]

        return res