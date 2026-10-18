class Solution:
    def findColoredRoot(self, edges: list[list[int]], colors: str) -> int:
        n = len(colors)
        indegree = [0] * n
        outdegree = [0] * n
        colorsMap = {
            'R' : 'B',
            'B' : 'W',
            'W' : 'R'
        }

        # colors give us directions
        for u, v in edges:
            if colorsMap[colors[u]] == colors[v]:
                outdegree[u] += 1 
                indegree[v] += 1
            elif colorsMap[colors[v]] == colors[u]:
                outdegree[v] += 1
                indegree[u] += 1
            else:
                return -1

        # validate
        root = -1
        for i in range(n):
            if indegree[i] > 1 or outdegree[i] > 2:
                return -1
            if indegree[i] == 0:
                root = i

        return root
            