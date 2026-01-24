class Logger:

    def __init__(self):
        self.store = {}        # msg -> ts

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.store or timestamp - self.store[message] >= 10:
            self.store[message] = timestamp
            return True
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)