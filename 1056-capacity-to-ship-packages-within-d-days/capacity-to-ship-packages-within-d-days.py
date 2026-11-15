class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def isValid(capacity):
            curDays, curSum = 1, 0
            for w in weights:
                curSum += w
                if curSum > capacity:
                    curDays += 1
                    curSum = w
            return curDays <= days

        l, r = max(weights), sum(weights)
        while l < r:
            mid = l + (r - l) // 2
            if not isValid(mid):
                l = mid + 1
            else:
                r = mid

        return l
