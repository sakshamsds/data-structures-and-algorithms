class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return
        
        if self.rank[p1] > self.rank[p2]:
            p1, p2 = p2, p1

        self.parent[p1] = p2
        self.rank[p2] += self.rank[p1]


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # union find
        rows, cols = len(grid), len(grid[0])

        store, nodes = {}, 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    store[(r, c)] = nodes
                    nodes += 1
        if nodes == 0:
            return 0

        uf = UnionFind(nodes)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 1:
                    continue

                if r != rows - 1 and grid[r + 1][c] == 1:
                    uf.union(store[(r, c)], store[(r + 1, c)])

                if c != cols - 1 and grid[r][c + 1] == 1:
                    uf.union(store[(r, c)], store[(r, c + 1)])

        return max(uf.rank)
                    
        