class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        
        def feasible(days):
            i = 0
            bouquets = 0
            while i < len(bloomDay) - k + 1:
                if bloomDay[i] > days:
                    i += 1
                    continue
                bouquets += 1
                for j in range(k):
                    if bloomDay[i + j] > days:
                        bouquets -= 1
                        break
                i += j + 1
            return bouquets >= m

        l, r = 1, max(bloomDay)
        while l < r:
            mid = l + (r - l) // 2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        
        return l