class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)
        if p1 == p2:
            return 0
        
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = self.parent[p1]
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = self.parent[p2]
            self.rank[p2] += self.rank[p1]
        return 1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # make nodes
        rows, cols = len(grid), len(grid[0])

        idx = 0
        d = {}
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    d[(r, c)] = idx
                    idx += 1
        
        num_nodes = idx
        uf = UnionFind(num_nodes)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    if r > 0 and grid[r - 1][c] == '1':
                        num_nodes -= uf.union(d[(r, c)], d[(r - 1, c)])
                    if c > 0 and grid[r][c - 1] == '1':
                        num_nodes -= uf.union(d[(r, c)], d[(r, c - 1)])

        return num_nodes