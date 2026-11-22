class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        jobs = [[d, p] for d, p in zip(difficulty, profit)]
        jobs.sort()
        for i in range(1, len(jobs)):
            jobs[i][1] = max(jobs[i][1], jobs[i - 1][1])

        totalProfit = 0 
        for w in worker:
            # binary search to find largest difficultly <= w
            l, r = 0, len(jobs)
            while l < r:
                mid = l + (r - l) // 2
                if jobs[mid][0] <= w:
                    l = mid + 1
                else:
                    r = mid
            if l > 0:
                totalProfit += jobs[l - 1][1] 

        return totalProfit
            
