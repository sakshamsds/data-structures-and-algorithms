class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # create adj list
        # dfs
        adj_list = collections.defaultdict(list)
        for src, dst in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)
        # print(adj_list)

        visited = set()
        def dfs(node):
            # print(node)
            visited.add(node)
            if node == destination:     # base case
                return True
            for nbr in adj_list[node]:
                if nbr not in visited and dfs(nbr):
                    return True
            return False

        return dfs(source)