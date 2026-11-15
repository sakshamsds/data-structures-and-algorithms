class Graph:

    def __init__(self, n: int, edges: list[list[int]]):
        self.adjList = collections.defaultdict(list)
        for src, dst, cost in edges:
            self.adjList[src].append((dst, cost))
        self.n = n

    def addEdge(self, edge: list[int]) -> None:
        src, dst, cost = edge
        self.adjList[src].append((dst, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        distances = [float('inf')] * self.n
        minHeap = [(0, node1)]
        visited = set()
        while minHeap:
            dist, node = heapq.heappop(minHeap)
            if node == node2:
                return dist
            if dist > distances[node]:
                continue
            for nbr, nbrCost in self.adjList[node]:
                if dist + nbrCost < distances[nbr]:     # reached nbr more optimally
                    distances[nbr] = dist + nbrCost
                    heapq.heappush(minHeap, (dist + nbrCost, nbr))
        return -1



# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)