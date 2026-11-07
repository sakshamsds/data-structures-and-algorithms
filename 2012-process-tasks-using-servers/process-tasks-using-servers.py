class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)

        busy = []           # t, w, i
        serverUsed = []
        t = 0
        for i, task in enumerate(tasks):
            t = max(i, t)
            if not available:       # all busy
                t = busy[0][0]

            while busy and busy[0][0] == t:
                _, w, i = heapq.heappop(busy)
                heapq.heappush(available, (w, i))

            w, i = heapq.heappop(available)
            serverUsed.append(i)
            heapq.heappush(busy, (t + task, w, i))

        return serverUsed