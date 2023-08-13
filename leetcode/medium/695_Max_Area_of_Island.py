# from queue import Queue
# q = Queue()
# q.put()   # add op
# q.get()   # pop op
# q.empty() # empty op

from typing import List

class Solution:

    # neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def dfs(r, c):
            if (
                r < 0 or r >= m or
                c < 0 or c >= n or
                grid[r][c] == 0 or
                (r, c) in visited
            ):
                return 0
            visited.add((r, c))
            return (1 + dfs(r - 1, c) +
                        dfs(r + 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))

        for i in range(m):
            for j in range(n):
                node = (i, j)
                if grid[i][j] == 1 and node not in visited:
                        island_area = dfs(i, j)
                        # island_area = self.dfs(node, grid, visited)
                        # island_area = self.bfs(node, grid, visited)
                        max_area = max(island_area, max_area)

        return max_area

    # def dfs(self, node, grid, visited):
    #     visited.add(node)
    #     area = 1
    #     for neighbor in self.neighbors:
    #         nbr_node = (node[0] + neighbor[0], node[1] + neighbor[1])
            
    #         # validate nbr_node
    #         if(
    #             nbr_node[0] < 0 or
    #             nbr_node[0] >= len(grid) or
    #             nbr_node[1] < 0 or
    #             nbr_node[1] >= len(grid[0]) or
    #             grid[nbr_node[0]][nbr_node[1]] == 0
    #         ):
    #             continue
            
    #         if nbr_node not in visited:
    #             visited.add(nbr_node)
    #             area += self.dfs(nbr_node, grid, visited)

    #     return area

    # def bfs(self, node, grid, visited):
    #     area = 0
    #     q = Queue()
    #     q.put(node)
    #     visited.add(node)

    #     while not q.empty():
    #         cur_node = q.get()
    #         # print(list(q.queue))
    #         area += 1

    #         for neighbor in self.neighbors:
    #             nbr_node = (cur_node[0] + neighbor[0], cur_node[1] + neighbor[1])
                
    #             # validate nbr_node
    #             if (
    #                 nbr_node[0] < 0 or
    #                 nbr_node[0] >= len(grid) or
    #                 nbr_node[1] < 0 or
    #                 nbr_node[1] >= len(grid[0]) or 
    #                 grid[nbr_node[0]][nbr_node[1]] == 0
    #             ):
    #                 continue

    #             if nbr_node not in visited:
    #                 q.put(nbr_node)
    #                 visited.add(nbr_node)

    #     return area 
