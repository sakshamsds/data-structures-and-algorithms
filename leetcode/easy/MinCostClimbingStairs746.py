from typing import List

# https://leetcode.com/problems/min-cost-climbing-stairs/
# https://www.youtube.com/watch?v=ktmzAZWkEZ0

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # calculate cost at every step
        num_steps = len(cost)

        for i in range(2, num_steps):
            cost[i] += min(cost[i-1], cost[i-2])
            # print(cost)

        return min(cost[num_steps-1], cost[num_steps-2])


inst = Solution()
print(inst.minCostClimbingStairs([10, 15, 20]))
# print(inst.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
print(inst.minCostClimbingStairs([0, 1, 2, 2]))

