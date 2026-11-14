class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)
        if p1 == p2:
            return 0

        if self.rank[p2] < self.rank[p1]:
            p1, p2 = p2, p1

        self.parent[p1] = p2
        self.rank[p2] += self.rank[p1]
        return 1


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        uf = UnionFind(n)
        components = n
        for start, end in edges:
            components -= uf.union(start, end)

        # print(components)
        return components == 1

        