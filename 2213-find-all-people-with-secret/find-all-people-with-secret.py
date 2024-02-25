class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        time_map = {}
        for x, y, time in meetings:
            if time not in time_map:
                time_map[time] = collections.defaultdict(list)
            time_map[time][x].append(y)
            time_map[time][y].append(x)
        
        secrets = set([0, firstPerson])

        def dfs(node):
            if node in visited:
                return
            secrets.add(node)
            visited.add(node)
            for nbr in adj[node]:
                dfs(nbr)

        for t in sorted(time_map.keys()):
            visited = set()
            adj = time_map[t]
            for src in adj:
                if src in secrets:
                    dfs(src)

        return list(secrets)