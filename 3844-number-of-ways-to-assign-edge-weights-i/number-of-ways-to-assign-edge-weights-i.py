class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        # find max depth

        # dp[i] = dp[i - 1]
        MOD = 1_000_000_007

        adjList = collections.defaultdict(list)
        for s, e in edges:
            adjList[s].append(e)
            adjList[e].append(s)

        def dfs(node):
            visited.add(node)
            depth = 0            
            for nbr in adjList[node]:
                if nbr not in visited:
                    depth = max(depth, 1 + dfs(nbr))
            return depth


        visited = set()
        depth = dfs(1)

        return 2 ** (depth - 1) % MOD