'''
    cost1 + cost2 < both
    cost1 + cost2 >= both
    min(cost1, cost2) > both, use both to get all
'''

class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        totalCost = min(need1, need2) * min(costBoth, cost1 + cost2)
        if need1 > need2:
            totalCost += (need1 - need2) * min(cost1, costBoth)
        else:
            totalCost += (need2 - need1) * min(cost2, costBoth)

        return totalCost