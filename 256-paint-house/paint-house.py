'''
R   17  18   
B   2   33  10 
G   17  7
'''

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        prev_costs = [0, 0, 0]

        for cur_r, cur_b, cur_g in costs:
            new_costs = [0, 0, 0]
            new_costs[0] = cur_r + min(prev_costs[1], prev_costs[2])
            new_costs[1] = cur_b + min(prev_costs[0], prev_costs[2])
            new_costs[2] = cur_g + min(prev_costs[0], prev_costs[1])
            prev_costs = new_costs
        
        return min(new_costs)
        

        