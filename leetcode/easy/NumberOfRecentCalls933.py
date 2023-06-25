from collections import deque

class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        for _ in range(len(self.q)):
            if t - self.q[-1] > 3000:
                self.q.pop()
            else:
                break
        self.q.appendleft(t)
        return len(self.q)
        


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
print(obj.ping(1))
print(obj.q)
print(obj.ping(100))
print(obj.q)
print(obj.ping(3001))
print(obj.q)
print(obj.ping(3002))
print(obj.q)
print(obj.ping(5000))
print(obj.q)
