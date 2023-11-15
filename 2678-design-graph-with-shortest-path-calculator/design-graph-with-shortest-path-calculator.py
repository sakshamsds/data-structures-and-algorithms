class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.adj_list = collections.defaultdict(list)
        for start, end, cost in edges:
            self.adj_list[start].append((end, cost))
        self.n = n

    def addEdge(self, edge: List[int]) -> None:
        start, end, cost = edge
        self.adj_list[start].append((end, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        # apply dijkstra
        distances = [float('inf')] * self.n
        pq = [(0, node1)]
        distances[node1] = 0        # distance to sources node = 0

        while pq:
            dist, node = heapq.heappop(pq)
            for nbr, edge_weight in self.adj_list[node]:
                if dist + edge_weight < distances[nbr]:
                    distances[nbr] = dist + edge_weight
                    heapq.heappush(pq, (distances[nbr], nbr))

        if distances[node2] == float('inf'):
            return -1
        return distances[node2] 
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)