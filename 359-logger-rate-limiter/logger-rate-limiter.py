class Logger:

    def __init__(self):
        self.uniques = set()
        self.q = collections.deque()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while self.q and timestamp - self.q[0][0] >= 10:
            _, msg = self.q.popleft()
            self.uniques.remove(msg)

        if message not in self.uniques:
            self.uniques.add(message)
            self.q.append((timestamp, message))
            return True

        return False




# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)