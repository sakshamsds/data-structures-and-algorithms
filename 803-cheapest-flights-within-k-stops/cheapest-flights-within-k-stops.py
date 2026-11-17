class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        
        # TC - O(n**2 + nklognk)
        # SC - O(n**2 + nk)

        adjList = collections.defaultdict(list)
        for u, v, p in flights:
            adjList[u].append((v, p))

        # dist, stops
        minHeap = [(0, -1, src)]  # dist, stops, node
        visited = set()
        visited = {
            (src, 0): 0     # node, stops -> cost
        }        

        while minHeap:
            dist, stops, node = heapq.heappop(minHeap)
            if node == dst:
                return dist

            if stops == k:      # can't process nbrs anymore
                continue

            for nbr, nbrCost in adjList[node]:
                newCost = dist + nbrCost
                newStops = stops + 1
                if (nbr, newStops) not in visited or visited[(nbr, newStops)] > newCost:
                    visited[(nbr, newStops)] = newCost
                    heapq.heappush(minHeap, (newCost, newStops, nbr))

        return -1
