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
    def largestIsland(self, grid: list[list[int]]) -> int:
        # union find
        rows, cols = len(grid), len(grid[0])
        nodes = {}
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    nodes[(r, c)] = count
                    count += 1

        uf = UnionFind(count)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue

                # check below
                if r < rows - 1 and grid[r + 1][c] == 1:
                    uf.union(nodes[(r, c)], nodes[(r + 1, c)])
                
                # check right
                if c < cols - 1 and grid[r][c + 1] == 1:
                    uf.union(nodes[(r, c)], nodes[(r, c + 1)])

        def getArea(nr, nc):
            parent = uf.find(nodes[(nr, nc)])
            area = uf.rank[parent]
            if parent not in curParents:
                curParents.add(parent)
                return area
            return 0

        largest = max(uf.rank) if count > 0 else 0     # bug 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    continue

                curArea = 1
                curParents = set()
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if (
                        nr < 0 or nr == rows or
                        nc < 0 or nc == cols or 
                        grid[nr][nc] == 0           # bug 2
                    ):
                        continue
                    curArea += getArea(nr, nc)

                largest = max(largest, curArea)
        return largest