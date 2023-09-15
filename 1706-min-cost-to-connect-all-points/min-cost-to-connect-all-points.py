class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        manhattan = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        n = len(points)
        adj = collections.defaultdict(list) # i: list of (cost, node)
        # create adj list
        for i in range(n):
            for j in range(i + 1, n):
                dist = manhattan(points[i], points[j])
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        # print(adj)
        
        # prim's algorithm
        res = 0
        visited = set()
        min_heap = [(0, 0)]         # start from zero node
        while len(visited) < n:     # while all nodes are not visited
            dist, i = heapq.heappop(min_heap)
            if i in visited:
                continue        # avoid cycles
            res += dist
            visited.add(i)
            for nbr_dist, nbr_node in adj[i]:       # add neighbors to heap
                if nbr_node not in visited:
                    heapq.heappush(min_heap, (nbr_dist, nbr_node))

        return res 

        