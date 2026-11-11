class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
    
        if p1 == p2:
            return 0

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] = self.rank[p1]
        return 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # r, c -> 0, 1 ,2
        store, count = {}, 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    store[(r, c)] = count
                    count += 1

        uf = UnionFind(count) 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != '1':
                    continue
                if c != cols - 1 and grid[r][c + 1] == '1':
                    count -= uf.union(store[(r, c)], store[(r, c + 1)])
                if r != rows - 1 and grid[r + 1][c] == '1':
                    count -= uf.union(store[(r, c)], store[(r + 1, c)])

        return count
            

