class Solution:
    def bestClosingTime(self, customers: str) -> int:
        shop_open_penalty = 0
        shop_closed_penalty = customers.count('Y')
        earliest_closing_hour, min_penalty = 0, shop_closed_penalty

        for i, customer in enumerate(customers):    # open shop at i
            if customer == "N":
                shop_open_penalty += 1
            else:
                shop_closed_penalty -= 1

            ith_penalty = shop_open_penalty + shop_closed_penalty
            if ith_penalty < min_penalty:
                earliest_closing_hour, min_penalty = i + 1, ith_penalty
        
        return earliest_closing_hour
            
 

            
