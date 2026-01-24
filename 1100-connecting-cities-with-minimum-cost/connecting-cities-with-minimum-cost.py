class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        adj_list = collections.defaultdict(list)
        for s, e, c in connections:
            adj_list[s].append((e, c))
            adj_list[e].append((s, c))

        visited = set()      
        min_heap = [(0, connections[0][0])]

        # prims algorithm
        min_cost = 0
        while min_heap and len(visited) < n:
            cost, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            min_cost += cost
            for nbr, nbr_cost in adj_list[node]:
                if nbr not in visited:
                    heapq.heappush(min_heap, (nbr_cost, nbr))
        
        # print(visited)
        return min_cost if len(visited) == n else -1