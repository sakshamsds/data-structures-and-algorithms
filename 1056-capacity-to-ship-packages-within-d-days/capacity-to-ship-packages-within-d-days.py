class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # define search range, use brute force, optimize with binary search
        l, r = max(weights), sum(weights)
        res = r

        while l <= r:
            cap = l + (r - l)//2

            time_taken = 0
            cur_w = 0
            for weight in weights:
                if cur_w + weight > cap:
                    time_taken += 1
                    cur_w = weight
                elif cur_w + weight == cap:
                    time_taken += 1
                    cur_w = 0
                else:
                    cur_w += weight
            
            if cur_w > 0:
                time_taken += 1

            # print(cap, time_taken)

            if time_taken > days:   # cannot have more days
                l = cap + 1
            else:                   # can have less days
                res = min(res, cap)
                r = cap - 1

        return res

