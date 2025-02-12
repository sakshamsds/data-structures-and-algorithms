'''
1   2
5   9
3   4
'''

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        k = len(costs[0])

        def getMinIdx(idx):
            min1, min2 = 2_000, 2_000
            for i, cost in enumerate(costs[idx]):
                if cost <= min1:
                    min1, min2 = cost, min1
                elif cost < min2:
                    min2 = cost
            return min1, min2

        for i in range(1, len(costs)):
            min1, min2 = getMinIdx(i - 1)
            for j in range(k):
                if min1 == costs[i - 1][j]:
                    costs[i][j] += min2
                else:
                    costs[i][j] += min1

        return min(costs[-1])