'''
    for every new meeting
    see if any used meeting is over (heap [endTime, roomNum])
        - add to available
    choose lowest from available rooms (heap [roomNum])

    TC - O(M * logN + M * logM) - O(M * logNM)
    SC - O(N)
'''

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort(key=lambda x: x[0])   # sort by the start time

        free = list(range(n))       # roomNum
        heapq.heapify(free)
        busy = []       # (endTime, roomNum)
        freqs = [0] * n

        for start, end in meetings:
            while busy and busy[0][0] <= start:
                heapq.heappush(free, heapq.heappop(busy)[1])

            if free:
                roomNum = heapq.heappop(free)
                heapq.heappush(busy, (end, roomNum))
            else:
                endTime, roomNum = heapq.heappop(busy)
                duration = end - start
                heapq.heappush(busy, (endTime + duration, roomNum))
            freqs[roomNum] += 1

        mostFreq, resNum = freqs[0], 0
        for roomNum, freq in enumerate(freqs):
            if freq > mostFreq:
                mostFreq, resNum = freq, roomNum
            
        return resNum