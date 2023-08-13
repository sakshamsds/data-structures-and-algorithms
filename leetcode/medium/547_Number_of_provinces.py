from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        # O(n ^ 2)
        n = len(isConnected)
        parent = [i for i in range(n)]
        rank = [1] * n
        
        def find(n1):               # parent of n1
            while n1 != parent[n1]:       # not pointing to itself
                parent[n1] = parent[parent[n1]]   # optimization
                n1 = parent[n1]
            return n1

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0

            if rank[p2] > rank[p1]:     # union by rank, add smaller to bigger tree
                parent[p1] = p2
                rank[p2] += rank[p1] 
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1

        res = n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    res -= union(i, j)

        return res

    # DFS 
    #     # convert to adjacency list
    #     adj_list = [[] for _ in range(len(isConnected))]
    #     for i in range(len(adj_list)):
    #         for j in range(len(adj_list)):
    #             if isConnected[i][j] == 1 and i != j:
    #                 adj_list[i].append(j)

    #     # print(adj_list)
    #     visited = set()

    #     count = 0
    #     for node in range(len(isConnected)):
    #         if node not in visited:
    #             self.dfs(node, adj_list, visited)
    #             count += 1

    #     return count

    # # can use bfs also
    # def dfs(self, node, adj_list, visited):
    #     visited.add(node)
    #     for neighbor in adj_list[node]:
    #         if neighbor not in visited:
    #             self.dfs(neighbor, adj_list, visited)

