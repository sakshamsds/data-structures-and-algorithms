class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour < len(dist) - 1:
            return -1

        def getTime(speed):
            arrival_time = 0
            for i in range(len(dist) - 1):
                arrival_time += ceil(dist[i]/speed)
            return arrival_time + dist[-1]/speed

        l, r = 1, max(dist) * 100
        while l < r:
            mid = l + (r - l) // 2
            arr_time = getTime(mid)
            if arr_time > hour:
                l = mid + 1
            else:
                r = mid

        return l if getTime(l) <= hour else -1