class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # graph is connected
        # graph has no cycle

        adj_list = collections.defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

    
        visited = set()
        def dfs(node, prev):        # detect cycle
            if node in visited:
                return False         # cycle detected

            visited.add(node)
            for nbr in adj_list[node]:
                if nbr != prev:
                    if not dfs(nbr, node):
                        return False
            return True

        return dfs(0, -1) and n == len(visited)