class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        numBombs = len(bombs)

        # directed graph, O(n ** 2)
        adjList = collections.defaultdict(list)

        for i in range(numBombs):
            x1, y1, r1 = bombs[i]
            for j in range(numBombs):
                if i == j:
                    continue
                x2, y2, _ = bombs[j]
                if r1 ** 2 >= (x1 - x2) ** 2 + (y1 - y2) ** 2:
                    adjList[i].append(j)


        def dfs(node) -> int:       # num explosions
            exploded.add(node)
            explosions = 1
            for nbr in adjList[node]:
                if nbr not in exploded:
                    explosions += dfs(nbr)
            return explosions

        # O(n * (V + E), v = n, e = n ** 2, -> n ** 3)
        maxExplosions = 0
        for i in range(numBombs):
            exploded = set()
            maxExplosions = max(maxExplosions, dfs(i))

        return maxExplosions