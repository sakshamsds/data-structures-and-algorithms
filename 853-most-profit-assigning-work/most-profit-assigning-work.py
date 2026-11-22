class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        jobs = [(d, p) for d, p in zip(difficulty, profit)]
        jobs.sort()
        worker.sort()

        i = 0
        totalProfit = maxProfit = 0
        for w in worker:
            while i < len(jobs) and jobs[i][0] <= w:
                maxProfit = max(maxProfit, jobs[i][1])
                i += 1
            totalProfit += maxProfit
        return totalProfit
            
