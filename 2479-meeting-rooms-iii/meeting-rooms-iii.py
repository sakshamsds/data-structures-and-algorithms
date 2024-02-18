class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        free_rooms = list(range(n))     # heap: room_num
        occupied_rooms = []     # heap: (end_time, room_num)
        num_meetings = [0] * n      # array: meetings
        meetings.sort()
        # print(meetings)

        for start, end in meetings:
            # free up rooms before cur start
            while occupied_rooms and occupied_rooms[0][0] <= start:
                heapq.heappush(free_rooms, heapq.heappop(occupied_rooms)[1])
            # print('free_rooms', free_rooms)

            if free_rooms:      # free_rooms available
                room_num = heapq.heappop(free_rooms)
            else:           # pop from occupied rooms
                prev_end, room_num = heapq.heappop(occupied_rooms)
                end += prev_end - start
            heapq.heappush(occupied_rooms, (end, room_num))
            num_meetings[room_num] += 1
            # print("occupied_rooms", occupied_rooms)
        
        # print(num_meetings)
        mx_meetings, res = -1, -1
        for room_num, meetings in enumerate(num_meetings):
            if meetings > mx_meetings:
                mx_meetings, res = meetings, room_num
        return res