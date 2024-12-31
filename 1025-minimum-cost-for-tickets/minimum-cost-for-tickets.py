class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # for every day we have 3 choices

        num_days = len(days)
        cache = {}

        def dfs(i):
            if i == len(days):
                return 0

            if i in cache:
                return cache[i]
            
            # pick one day pass
            cur_cost = costs[0] + dfs(i + 1)

            # pick 7 day pass
            j = i + 1
            while j < num_days and days[j] <= days[i] + 6:
                j += 1
            cur_cost = min(cur_cost, costs[1] + dfs(j))

            # pick 30 day pass
            j = i + 1
            while j < num_days and days[j] <= days[i] + 29:
                j += 1
            cur_cost = min(cur_cost, costs[2] + dfs(j))

            cache[i] = cur_cost
            return cur_cost

        return dfs(0)