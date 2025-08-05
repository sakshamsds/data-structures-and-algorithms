class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:

        restricted = set(restricted)
        
        adj_list = collections.defaultdict(list)
        for s, e in edges:
            adj_list[s].append(e)
            adj_list[e].append(s)

        visited = set([0])
        q = collections.deque([0])

        while q:
            cur_node = q.popleft()
            for nbr in adj_list[cur_node]:
                if nbr in visited or nbr in restricted:
                    continue
                q.append(nbr)
                visited.add(nbr)

        return len(visited)