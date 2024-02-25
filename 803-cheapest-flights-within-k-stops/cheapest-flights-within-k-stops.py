class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for _ in range(k + 1):
            tmp_prices = prices.copy()
            for f, t, p in flights:
                tmp_prices[t] = min(tmp_prices[t], prices[f] + p)
            prices = tmp_prices

        return -1 if prices[dst] == float('inf') else prices[dst]
