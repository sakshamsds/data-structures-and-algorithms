class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # most stones removed = total - number of connected components

        n = len(stones)

        # represent the graph
        adjList = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    adjList[i].append(j)
                    adjList[j].append(i)

        # print(adjList)
        visited = set()

        def dfs(cur_stone):
            visited.add(cur_stone)
            for nbr in adjList[cur_stone]:
                if nbr not in visited:
                    dfs(nbr)

        # get number of connected components
        num_comps = 0
        for stone in range(n):
            if stone not in visited:
                dfs(stone)
                num_comps += 1

        return n - num_comps