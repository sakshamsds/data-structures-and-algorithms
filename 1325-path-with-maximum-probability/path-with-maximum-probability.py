class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # take log of prob
        # use -values to use dijkstra's shortest path problem

        adjList = defaultdict(list)
        for i, (src, dst) in enumerate(edges):
            adjList[src].append((dst, succProb[i]))
            adjList[dst].append((src, succProb[i]))

        pq = [(-1, start_node)]
        visited = set()

        while pq:
            prob, cur = heapq.heappop(pq)
            visited.add(cur)
            if cur == end_node:
                return prob * -1
            for nbr, edgeProb  in adjList[cur]:
                if nbr not in visited:
                    heapq.heappush(pq, (prob * edgeProb, nbr))
                
        return 0



