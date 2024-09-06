'''
You're building the graph one edge at a time. 
However, before adding an edge between u and v, 
you first check if there already is a path between them, avoiding a cycle.
'''

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        adjList = collections.defaultdict(list)

        def dfs(u, v):
            if u == v:
                return True
            
            for nbr in adjList[u]:
                if nbr not in visited:
                    visited.add(nbr)
                    if dfs(nbr, v):
                        return True

            return False
            
        res = []
        for u, v in edges:
            visited = set([u])
            if dfs(u, v):
                res = [u, v]
            adjList[u].append(v)
            adjList[v].append(u)

        return res