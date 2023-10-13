class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):   # find aggregate cost at every step
            cost[i] += min(cost[i - 1], cost[i - 2])

        return min(cost[-1], cost[-2])