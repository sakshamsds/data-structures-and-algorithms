'''
    start, duration

    (duration, idx, start)   -> heap

    # sort by start time
    TC - O(NlogN)
    SC- O(N)
'''

class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        pending = deque(sorted([(s, d, i) for i, (s, d) in enumerate(tasks)]))
        available, processed, endTime = [], [], 0

        while pending or available:
            if not available and endTime < pending[0][0]:     # cpu idle time
                endTime = pending[0][0]
            while pending and pending[0][0] <= endTime:
                _, d, i = pending.popleft()
                heapq.heappush(available, (d, i))
            d, i = heapq.heappop(available)
            processed.append(i)
            endTime += d
        
        return processed