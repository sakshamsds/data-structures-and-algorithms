'''
    start, duration

    (duration, idx, start)   -> heap

    # sort by start time
    TC - O(NlogN)
    SC- O(N)
'''

class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        nextTask = []        # duration, idx
        endTime, i = 0, 0
        processed = []
        newOrder = [(t[0], t[1], i) for i, t in enumerate(tasks)]
        newOrder.sort(key=lambda x: (x[0], x[1]))

        while nextTask or i < len(newOrder):        # len(processed) < len(tasks)
            if not nextTask and endTime < newOrder[i][0]:     # cpu idle time
                endTime = newOrder[i][0]
            while i < len(newOrder) and newOrder[i][0] <= endTime:
                heapq.heappush(nextTask, (newOrder[i][1], newOrder[i][2]))
                i += 1
            # tasks are in heap
            duration, idx = heapq.heappop(nextTask)
            processed.append(idx)
            endTime += duration
        
        return processed