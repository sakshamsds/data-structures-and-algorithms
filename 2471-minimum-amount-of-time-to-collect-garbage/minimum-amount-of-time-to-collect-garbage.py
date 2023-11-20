'''
G -> P -> GP -> GG
   2    4     3
G -> 0 + 1 + 2 + 4 + 1 + 3 + 2 = 13
P -> 0 + 2 + 1 + 4 + 1 = 8
M ->

travel to all the houses
if house contains M, add the travel time as well
'''

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:

        def get_cost(g_type):
            time_taken = 0
            last_house = -1
            for i in range(len(garbage)):
                count = garbage[i].count(g_type)
                if count > 0:
                    last_house = i
                time_taken += count

            travel_cost = 0
            if last_house > 0:   # either not found or found at 0 house   
                travel_cost = sum(travel[:last_house])

            return travel_cost + time_taken

        return get_cost('G') + get_cost('M') + get_cost('P')