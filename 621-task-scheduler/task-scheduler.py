class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # pick the most popular task
        # maintain a queue
        # TC - NlogN
        # SC - N

        available = [(-freq, task) for task, freq in collections.Counter(tasks).items()]
        heapq.heapify(available)
        cooldown = deque()      # nextAvailability, -freq, task

        interval = 0
        while available or cooldown:
            if not available:
                interval = max(interval, cooldown[0][0])

            while cooldown and cooldown[0][0] <= interval:
                _, freq, task = cooldown.popleft()
                heapq.heappush(available, (freq, task))

            freq, task = heapq.heappop(available)
            # print(interval, task)
            if freq < -1:
                cooldown.append((interval + n + 1, freq + 1, task))
            interval += 1
        return interval
            