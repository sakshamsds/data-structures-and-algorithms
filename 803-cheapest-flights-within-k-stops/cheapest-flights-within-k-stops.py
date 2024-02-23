class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        for _ in range(k + 1):
            temp = prices.copy()
            for f, t, p in flights:
                if prices[f] == float('inf'):
                    continue
                temp[t] = min(temp[t], prices[f] + p)
            prices = temp
        # print(prices)
        return prices[dst] if prices[dst] != float('inf') else -1