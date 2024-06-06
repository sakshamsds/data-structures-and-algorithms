class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        counts = collections.Counter(nums)
        minHeap = []
        for num, freq in counts.items():
            minHeap.append((num, freq))
        heapq.heapify(minHeap)

        while minHeap:
            tmpFreqs = []
            prevNum = None

            for _ in range(k):
                if not minHeap:
                    return False
                curNum, freq = heapq.heappop(minHeap)
                if prevNum is not None and prevNum + 1 != curNum:
                    return False
                if freq > 1:
                    tmpFreqs.append((curNum, freq - 1))
                prevNum = curNum

            for num, freq in tmpFreqs:
                heapq.heappush(minHeap, (num, freq))

        return True