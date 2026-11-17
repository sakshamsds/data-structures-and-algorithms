class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:

        prices = [float('inf')] * n
        prices[src] = 0

        for _ in range(k + 1):
            newPrices = prices.copy()
            for u, v, p in flights:
                if prices[u] != float('inf'):        # can travel here            
                    newPrices[v] = min(newPrices[v], prices[u] + p)
            prices = newPrices

        return -1 if prices[dst] == float('inf') else prices[dst]