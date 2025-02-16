class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l < r:
            capacity = l + (r - l) // 2

            current_load = 0
            days_needed = 1
            for weight in weights:
                if current_load + weight > capacity:
                    days_needed += 1
                    current_load = 0
                current_load += weight
                if days_needed > days:          # early termination
                    break

            if days_needed <= days:
                r = capacity
            else:
                l = capacity + 1
        return l