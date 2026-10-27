class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # go through every edge again and again
        # k = 0 means first iteration, direct flights

        # initialize the distances to be infinite
        prices = [float('inf')] * n
        prices[src] = 0

        for _ in range(k + 1):      # since k = 0 means one iteration
            new_prices = prices.copy()
            for start, end, price in flights:       # iterate each edge
                if prices[start] != float('inf'):       # can we reach this start
                    new_prices[end] = min(new_prices[end], prices[start] + price)
            prices = new_prices
            
        return -1 if prices[dst] == float('inf') else prices[dst]