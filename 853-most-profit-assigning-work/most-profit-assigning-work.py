class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        maxW = max(worker)
        jobs = [0] * (maxW + 1)     # max profit at that difficulty

        for d, p in zip(difficulty, profit):
            if d <= maxW:
                jobs[d] = max(jobs[d], p)

        for j in range(1, len(jobs)):
            jobs[j] = max(jobs[j], jobs[j - 1])

        totalProfit = 0
        for w in worker:
            totalProfit += jobs[w]
        return totalProfit