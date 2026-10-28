class MyCalendarTwo:

    def __init__(self):
        self.events = sortedcontainers.SortedDict()         # O(logN) insertion, lookup, deletion

    def book(self, startTime: int, endTime: int) -> bool:
        self.events[startTime] = self.events.get(startTime, 0) + 1
        self.events[endTime] = self.events.get(endTime, 0) - 1

        prefix = 0
        for event in self.events.values():
            prefix += event
            if prefix == 3:
                # rollback
                self.events[startTime] -= 1
                self.events[endTime] += 1

                if self.events[startTime] == 0:
                    self.events.pop(startTime)
                if self.events[endTime] == 0:
                    self.events.pop(endTime)
                return False

        return True



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)