class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        min_heap = [-1]       # end times

        for s, e in intervals:
            if min_heap[0] <= s:         # assign to the room where meeting has ended
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, e)

        return len(min_heap)