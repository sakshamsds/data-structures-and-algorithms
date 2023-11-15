'''
pass through all the vertices available, dp
2 -> 5
    : 2 -> 1 + 1 -> 5
    : 2 -> 2 + 2 -> 5
            .
            .
            .
    : 2 -> n + n -> 5
'''

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        # make adj matrix
        self.adj_matrix = [[float('inf')] * n for _ in range(n)]
        for start, end, cost in edges:
            self.adj_matrix[start][end] = cost 

        for i in range(n): 
            self.adj_matrix[i][i] = 0

        # floyd warshall
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    self.adj_matrix[i][j] = min(self.adj_matrix[i][j], 
                                                self.adj_matrix[i][via] + 
                                                self.adj_matrix[via][j])

    def addEdge(self, edge: List[int]) -> None:
        start, end, cost = edge
        n = len(self.adj_matrix)

        # via node becomes start -> end
        for i in range(n):
            for j in range(n):
                self.adj_matrix[i][j] = min(self.adj_matrix[i][j], 
                                            self.adj_matrix[i][start] + 
                                            cost + 
                                            self.adj_matrix[end][j])

    def shortestPath(self, node1: int, node2: int) -> int:
        cost = self.adj_matrix[node1][node2]
        return -1 if cost == float('inf') else cost


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)