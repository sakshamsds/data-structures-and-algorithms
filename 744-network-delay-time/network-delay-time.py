class Solution:
    def networkDelayTime(self, edges: list[list[int]], n: int, k: int) -> int:
        times = [float('inf')] * (n + 1)
        times[0] = 0
        times[k] = 0
        for _ in range(n):  
            new_times = times.copy()
            for u, v, w in edges:
                if times[u] != float('inf'):
                    new_times[v] = min(new_times[v], times[u] + w)
            times = new_times

        min_time = max(times)
        return -1 if min_time == float('inf') else min_time