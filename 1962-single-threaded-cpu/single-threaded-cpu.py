'''
    start, duration

    (duration, idx, start)   -> heap

    # sort by start time

'''

class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        tasks_available = []        # duration, idx
        self.i = 0
        endTime = 0
        processed = []
        newOrder = [(t[0], t[1], i) for i, t in enumerate(tasks)]
        newOrder.sort(key=lambda x: (x[0], x[1]))

        def addTask():
            while self.i < len(newOrder) and newOrder[self.i][0] <= endTime:
                heapq.heappush(tasks_available, (newOrder[self.i][1], newOrder[self.i][2]))
                self.i += 1
            

        while tasks_available or self.i < len(newOrder):        # len(processed) < len(tasks)
            addTask()
            if not tasks_available:     # cpu idle time
                endTime = newOrder[self.i][0]
                addTask()

            # tasks are in heap
            duration, idx = heapq.heappop(tasks_available)
            processed.append(idx)
            endTime += duration
        
        return processed