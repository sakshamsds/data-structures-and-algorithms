class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dist = [[float(inf)] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0

        # iterate edges
        for i in range(len(original)):
            u = ord(original[i]) - ord('a')
            v = ord(changed[i]) - ord('a')
            dist[u][v] = min(dist[u][v], cost[i])

        # floyd warshall
        for k in range(26):
            for u in range(26):
                for v in range(26):
                    dist[u][v] = min(dist[u][v], dist[u][k] + dist[k][v])

        total_cost = 0
        for i in range(len(source)):
            u = ord(source[i]) - ord('a')
            v = ord(target[i]) - ord('a')
            if dist[u][v] >= float(inf):
                return -1
            total_cost += dist[u][v]

        return total_cost