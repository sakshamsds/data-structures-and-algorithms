class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        N = len(points)
        res = 0
        visited = set()
        min_heap = [(0, 0)] 
        while len(visited) < N:
            dist, cur = heapq.heappop(min_heap)
            if cur in visited:
                continue
            visited.add(cur)

            res += dist
            for nbr in range(N):
                if nbr not in visited:
                    weight = abs(points[cur][0] - points[nbr][0]) + \
                            abs(points[cur][1] - points[nbr][1])
                    heapq.heappush(min_heap, (weight, nbr))

        return res