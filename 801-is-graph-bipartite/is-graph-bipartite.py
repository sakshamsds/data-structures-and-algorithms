class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        colors = dict()     # node -> color (0, 1)

        def bfs(node):
            if node in colors:
                return True
            q = deque([node])
            colors[node] = 0
            while q:
                cur = q.popleft()
                for nbr in graph[cur]:
                    if nbr not in colors:
                        colors[nbr] = colors[cur] ^ 1
                        q.append(nbr)
                    elif colors[nbr] == colors[cur]:
                        return False
            return True

        for i in range(len(graph)):     # graph might not be connected
            if not bfs(i):
                return False

        return True