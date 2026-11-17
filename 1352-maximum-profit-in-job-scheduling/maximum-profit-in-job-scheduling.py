class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        # print(intervals)

        # def dfs(i, prevEnd)   N**2
        cache = {}

        def dfs(i):
            if i >= len(intervals):
                return 0
            if i in cache:
                return cache[i]

            profit = dfs(i + 1)      # skip current job
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            profit = max(profit, dfs(j) + intervals[i][2])
            cache[i] = profit
            return profit

        return dfs(0)