class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # O(n * m), m -> idle time
        freqs = collections.Counter(tasks)
        maxHeap = [-cnt for cnt in freqs.values()]
        heapq.heapify(maxHeap)
        q = deque()     # pairs [-cnt, nextTime]
        time = 0

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time

