from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        busy = []       # end time, id
        free = SortedList(list(range(k)))
        count = [0] * k

        for i, t in enumerate(arrival):
            while busy and busy[0][0] <= t:
                _, serverNum = heapq.heappop(busy)
                free.add(serverNum)
            
            if free:
                idx = free.bisect_left(i % k)
                # severs[0....i] + servers[i + 1....n]
                serverUsed = free[idx] if idx < len(free) else free[0]
                free.remove(serverUsed)
                heapq.heappush(busy, (t + load[i], serverUsed))
                count[serverUsed] += 1
            
        maxJobs = max(count)
        return [i for i in range(k) if count[i] == maxJobs]
            