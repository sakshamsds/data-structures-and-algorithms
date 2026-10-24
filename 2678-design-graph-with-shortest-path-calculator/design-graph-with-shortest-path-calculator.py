# https://www.youtube.com/watch?v=4OQeCuLYj-4

# floyd warshall, negative weights are allowed

class Graph:

    def __init__(self, n: int, edges: list[list[int]]):
        # adj matrix
        # via -> source -> destination
        self.adj_matrix = [[float('inf')] * n for _ in range(n)]
        self.n = n
        for i in range(n):
            self.adj_matrix[i][i] = 0

        for u, v, dist in edges:
            self.adj_matrix[u][v] = dist 

        for via in range(n):
            for u in range(n):
                for v in range(n):
                    self.adj_matrix[u][v] = min(
                        self.adj_matrix[u][v],
                        self.adj_matrix[u][via] + self.adj_matrix[via][v]
                    )

    def addEdge(self, edge: list[int]) -> None:
        # s, e in edge
        # source -> s
        # e -> destination

        s, e, dist = edge
        for u in range(self.n):
            for v in range(self.n):
                self.adj_matrix[u][v] = min(
                    self.adj_matrix[u][v],
                    self.adj_matrix[u][s] + dist + self.adj_matrix[e][v]
                )

    def shortestPath(self, node1: int, node2: int) -> int:
        min_dist = self.adj_matrix[node1][node2]
        return min_dist if min_dist != float('inf') else -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)