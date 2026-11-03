'''
    dfs(i):
        pick 1 days pass
        pick 7 days pass
        pick 30 days pass
        # select next i
                        dfs(0)
            dfs(4)      dfs(8)      dfs(30)
'''

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cache = {}

        def dfs(i):
            if i == len(days):
                return 0
            if i in cache:
                return cache[i]

            j = i + 1
            min_cost = costs[0] + dfs(j)
            while j < len(days) and days[j] - days[i] <= 6:
                j += 1
            min_cost = min(min_cost, costs[1] + dfs(j))
            while j < len(days) and days[j] - days[i] <= 29:
                j += 1
            min_cost = min(min_cost, costs[2] + dfs(j))
            cache[i] = min_cost
            return min_cost

        return dfs(0)
