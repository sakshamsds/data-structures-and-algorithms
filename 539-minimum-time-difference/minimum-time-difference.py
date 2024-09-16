class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [0] * (24 * 60)
        for time in timePoints:
            h, m = map(int, time.split(':'))
            total_minutes = h * 60 + m
            if minutes[total_minutes]:
                return 0
            minutes[total_minutes] = 1

        l = -1
        first_time_idx = -1
        min_mins = 24 * 60
        for r in range(24 * 60):
            if not minutes[r]:
                continue
            if l > 0:
                min_mins = min(min_mins, r - l)
            l = r
            if first_time_idx == -1:
                first_time_idx = r

        return min(
            min_mins, 
            24 * 60 - l + first_time_idx
        )
            