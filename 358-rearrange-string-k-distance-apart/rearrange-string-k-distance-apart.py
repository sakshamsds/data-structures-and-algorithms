class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        # TC - (n + k)logk
        # SC - k
        if k <= 1:
            return s

        available = []      # freq, c
        cooldown = deque()       # nextAvailability, freq, c     # park in queue

        count = collections.Counter(s)
        for c, freq in count.items():
            available.append((-freq, c))
        heapq.heapify(available)

        res = []
        for i in range(len(s)):
            while cooldown and cooldown[0][0] <= i:
                _, freq, c = cooldown.popleft()
                heapq.heappush(available, (freq, c))

            if not available:
                return ""

            freq, c = heapq.heappop(available)
            res.append(c)
            if freq < -1:
                cooldown.append((i + k, freq + 1, c))

        return ''.join(res)