class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adjList = collections.defaultdict(list)
        for u, v, w in times:
            adjList[u].append((v, w))

        min_dist = [0] + [float('inf')] * n
        min_dist[k] = 0

        min_heap = [(0, k)]
        while min_heap:
            cur_dist, node = heapq.heappop(min_heap)
            for nbr, weight in adjList[node]:
                new_dist = cur_dist + weight
                if new_dist < min_dist[nbr]:
                    min_dist[nbr] = new_dist
                    heapq.heappush(min_heap, (new_dist, nbr))

        # print(min_dist)
        max_time = max(min_dist)
        return -1 if max_time == float('inf') else max_time