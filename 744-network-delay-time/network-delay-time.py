class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = collections.defaultdict(list)
        for s, d, w in times:
            adjList[s].append((d, w))
        # print(adjList)

        distances = [float('inf')] * (n + 1)
        distances[k] = 0
        pq = [(0, k)]

        while pq:
            dist, cur = heapq.heappop(pq)
            if dist > distances[cur]:
                continue
            for nbr, w in adjList[cur]:
                if dist + w < distances[nbr]:
                    distances[nbr] = dist + w
                    heapq.heappush(pq, (w + dist, nbr))
            
        # print(distances[1:])
        maxDist = max(distances[1:])
        return -1 if maxDist == float('inf') else maxDist