class MyCalendarThree:

    def __init__(self):
        self.events = sortedcontainers.SortedDict()

    def book(self, startTime: int, endTime: int) -> int:
        # not enough calls so better use sorted dict
        self.events[startTime] = self.events.get(startTime, 0) + 1
        self.events[endTime] = self.events.get(endTime, 0) - 1
        num_events = 0
        max_events = 0
        for _, e in self.events.items():
            num_events += e
            max_events = max(max_events, num_events)
        return max_events


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)