'''
    --------------
        ---------------------------
            -----
                        -------
                            ------
    0                                       30
        5   10
                    15          20
                        16          25
                            17          26


'''

class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        min_rooms = 1
        end_times = []

        for start, end in intervals:
            while end_times and end_times[0] <= start:
                heapq.heappop(end_times)    # meeting has ended, remove from queue
            heapq.heappush(end_times, end)
            min_rooms = max(min_rooms, len(end_times))

        return min_rooms