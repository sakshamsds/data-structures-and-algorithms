class Solution:
    def maxLength(self, ribbons: list[int], k: int) -> int:
        if k > sum(ribbons):
            return 0

        # binary search on the answer, ribbon length

        def isValid(maxLength):
            cuts = 0
            for ribbon in ribbons:
                cuts += ribbon // maxLength
            return cuts >= k

        l, r = 1, sum(ribbons)
        while l < r:
            mid = l + (r - l) // 2
            if isValid(mid):
                l = mid + 1
            else:
                r = mid

        return l - 1