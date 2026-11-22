class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        N = len(points)

        adjList = collections.defaultdict(list)     # node -> (nbr, dist)
        for u in range(N):
            for v in range(u + 1, N):
                dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                adjList[u].append((v, dist))
                adjList[v].append((u, dist))

        visited = set([0])
        minHeap = [(dist, v) for v, dist in adjList[0]]
        heapq.heapify(minHeap)

        minCost = 0
        while len(visited) != N:
            dist, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            # print(dist, node)
            minCost += dist
            visited.add(node)
            for nbr, nbrDist in adjList[node]:
                if nbr not in visited:
                    heapq.heappush(minHeap, (nbrDist, nbr))

        return minCost