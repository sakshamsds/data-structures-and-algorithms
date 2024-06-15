class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        tasks = []
        for c, p in zip(capital, profits):  # O(N*logN)
            tasks.append((c, p))
        tasks.sort()
        available_profits = []      # max_heap
        i = 0

        for _ in range(k):          
            while i < len(tasks) and tasks[i][0] <= w:
                heapq.heappush(available_profits, -tasks[i][1])
                i += 1
            if not available_profits:   # out of tasks
                break
            w += -heapq.heappop(available_profits)    # choose the biggest profit task 
        return w