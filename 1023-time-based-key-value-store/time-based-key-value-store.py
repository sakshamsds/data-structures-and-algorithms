class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)     # key -> (ts, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect_right(self.store[key], timestamp, key=lambda x:x[0])
        if idx == 0:
            return ""
        return self.store[key][idx - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)