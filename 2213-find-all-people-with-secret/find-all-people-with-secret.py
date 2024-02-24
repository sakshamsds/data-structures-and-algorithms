class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # O(n)
        # make graph for every timestep
        time_steps = {}
        for src, dst, t in meetings:
            if t not in time_steps:
                time_steps[t] = collections.defaultdict(list)
            time_steps[t][src].append(dst)
            time_steps[t][dst].append(src)

        secrets = set([0, firstPerson])

        def dfs(node, adj):
            if node in visited:
                return
            secrets.add(node)
            visited.add(node)
            for nbr in adj[node]:
                dfs(nbr, adj)

        # O(mlogm + n)
        for t in sorted(time_steps.keys()):
            visited = set()
            for node in time_steps[t]:
                if node in secrets:  # then only we can infect the secret
                    dfs(node, time_steps[t])

        return list(secrets)