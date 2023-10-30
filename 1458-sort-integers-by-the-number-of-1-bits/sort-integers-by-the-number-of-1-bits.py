class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        min_heap = []

        def getOnes(x):
            cnt = 0
            while x > 0:
                x = x & (x - 1)
                cnt += 1
            return cnt

        for num in arr:
            heapq.heappush(min_heap, (getOnes(num), num))

        res = []
        while min_heap:
            _, num = heapq.heappop(min_heap)
            res.append(num)

        return res