class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)

        if p1 == p2:
            return False

        if self.rank[p1] < self.rank[p2]:
            self.parents[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.parents[p2] = p1
            self.rank[p1] += self.rank[p2]
        return True

class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # no isolated nodes
        # no cycle  

        if len(edges) != n - 1:
            return False

        uf = UnionFind(n)
        for u, v in edges:
            if not uf.union(u, v):
                return False
            # print(uf.parents)
            # print(uf.rank)
        return True