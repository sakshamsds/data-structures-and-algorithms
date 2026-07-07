'''
    1           4
            3               6
        2                           8
'''

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : (x[1], -x[0]))
        # print(intervals)
        maxHeap = []        # contains start positions

        for s, _ in intervals:
            while maxHeap and -maxHeap[0] >= s:
                heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, -s)

        return len(maxHeap)

