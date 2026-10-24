class Graph:

    def __init__(self, n: int, edges: list[list[int]]):
        self.adjList = collections.defaultdict(list)
        for edge in edges:
            s, e, edge_weight = edge
            self.adjList[s].append((e, edge_weight))
        self.n = n

    def addEdge(self, edge: list[int]) -> None:
        s, e, edge_weight = edge
        self.adjList[s].append((e, edge_weight))        # nbr, edge_weight

    def shortestPath(self, node1: int, node2: int) -> int:
        distances = [float('inf')] * self.n
        distances[node1] = 0
        min_heap = [(0, node1)]     # dist from start, node

        while min_heap:
            dist, node = heapq.heappop(min_heap)
            if node == node2:
                return dist

            for nbr, edge_weight in self.adjList[node]:
                new_dist = dist + edge_weight
                if new_dist < distances[nbr]:
                    distances[nbr] = new_dist
                    heapq.heappush(min_heap, (new_dist, nbr))

        return -1



# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)