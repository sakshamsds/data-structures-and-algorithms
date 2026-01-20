class TimeMap:

    def __init__(self):
        self.map = collections.defaultdict(list)    # key -> [(timestamp, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        search_space = self.map[key]
        l, r = 0, len(search_space)

        while l < r:
            mid = l + (r - l) // 2
            mid_ts = search_space[mid][0]
            if mid_ts <= timestamp:
                l = mid + 1
            else:
                r = mid

        return "" if r == 0 else search_space[r - 1][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)