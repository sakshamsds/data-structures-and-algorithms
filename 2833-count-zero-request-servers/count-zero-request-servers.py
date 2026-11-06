class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda x: x[1])		# sort using the timestamps in increasing order

        ranges = [(q, i) for i, q in enumerate(queries)]
        ranges.sort(key=lambda x: x[0])

        inactiveServers = [0] * len(queries)
        activeFreq = {}

        l, r = 0, 0
        for q, i in ranges:
            start, end = q - x, q

            while r < len(logs) and logs[r][1] <= end:		
                serverId = logs[r][0]
                activeFreq[serverId] = activeFreq.get(serverId, 0) + 1
                r += 1

            while l < len(logs) and logs[l][1] < start:
                serverId = logs[l][0]
                activeFreq[serverId] -= 1
                if activeFreq[serverId] == 0:
                    activeFreq.pop(serverId)
                l += 1

            inactiveServers[i] = n - len(activeFreq)

        return inactiveServers