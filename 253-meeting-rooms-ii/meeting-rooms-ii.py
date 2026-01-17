class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        prev_ends = []
        max_rooms = 1

        for s, e in intervals:
            new_ends = []
            for pe in prev_ends:
                if s < pe:
                    new_ends.append(pe)
            new_ends.append(e)
            prev_ends = new_ends
            max_rooms = max(max_rooms, len(prev_ends))

        return max_rooms
        