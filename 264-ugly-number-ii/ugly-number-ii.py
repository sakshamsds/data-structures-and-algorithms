class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # generate ugly numbers 
        seen = set([1])
        min_ugly = [1]

        for _ in range(n):
            mn = heapq.heappop(min_ugly)
            for num in [2, 3, 5]:
                new_ugly = num * mn
                if new_ugly not in seen:
                    heapq.heappush(min_ugly, new_ugly)
                    seen.add(new_ugly)
        return mn
