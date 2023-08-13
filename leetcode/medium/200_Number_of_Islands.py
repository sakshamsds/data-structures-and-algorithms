from typing import List


class UnionFind:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.n = n
        self.size = n

    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi != pj:
            self.size -= 1
            self.p[pj] = pi

    def find(self, i):
        while i != self.p[i]:
            self.p[i] = self.p[self.p[i]]        # skip one level, path compression
            i = self.p[i]
        return i

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        n, m = len(grid), len(grid[0])
        d = dict()
        idx = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    d[i, j] = idx
                    idx += 1

        uf = UnionFind(idx)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    if i > 0 and grid[i-1][j] == '1':
                        uf.union(d[i-1, j], d[i, j])
                    if j > 0 and grid[i][j - 1] == '1':
                        uf.union(d[i, j-1], d[i, j])

        return uf.size


    # neighbors = [(0, 1), (-1, 0), (1, 0), (0,-1)]
    # # neighbors = [(-1, 1), (0, 1), (1, 1),
    # #              (-1, 0), (1, 0),
    # #              (-1,-1), (0,-1), (1,-1)]

    # def numIslands(self, grid: List[List[str]]) -> int:
    #     visited = set()
    #     count = 0
    #     for i in range(len(grid)):
    #         for j in range(len(grid[0])):
    #             node = (i, j)
    #             if grid[i][j] == '1' and node not in visited:
    #                 self.dfs(node, grid, visited)
    #                 count += 1
    #     return count

    # def dfs(self, node, grid, visited):
    #     visited.add(node)
    #     for neighbor in self.neighbors:
    #         nbr_node = (node[0] + neighbor[0], node[1] + neighbor[1])
    #         if (
    #             nbr_node[0] < 0 or 
    #             nbr_node[0] >= len(grid) or 
    #             nbr_node[1] < 0 or
    #             nbr_node[1] >= len(grid[0]) or
    #             grid[nbr_node[0]][nbr_node[1]] == '0'
    #         ):
    #             continue
    #         if nbr_node not in visited:
    #             self.dfs(nbr_node, grid, visited)

            

        