class Leaderboard:

    def __init__(self):
        self.map = collections.defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:  # log(n)
        self.map[playerId] += score

    def top(self, K: int) -> int:
        max_heap = []
        for p, s in self.map.items():
            heapq.heappush(max_heap, -s)
        topK = 0
        for _ in range(K):
            topK += heapq.heappop(max_heap)
        return -topK

    def reset(self, playerId: int) -> None:     # 1
        self.map.pop(playerId)


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)