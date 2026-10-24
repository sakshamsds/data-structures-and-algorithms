'''
    1   2   3   4   5
            l   r
'''


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        num_piles = len(piles)

        def canFinishBeforeTime(k):
            time_taken = 0
            for p in piles:
                time_taken += math.ceil(p / k)
            # print(k, time_taken)
            return time_taken <= h

        l, r = 1, max(piles)
        while l < r:
            mid = l + (r - l) // 2
            if canFinishBeforeTime(mid):
                r = mid
            else:
                l = mid + 1

        return l