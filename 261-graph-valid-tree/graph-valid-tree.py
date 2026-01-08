class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # graph is connected
        # graph has no cycle

        if n != len(edges) + 1:
            return False

        adj_list = collections.defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        q = collections.deque([0])
        visited = [False] * n
        visited[0] = True

        while q:
            cur = q.popleft()
            for nbr in adj_list[cur]:
                if not visited[nbr]:
                    q.append(nbr)
                    visited[nbr] = True
        
        return all(visited)