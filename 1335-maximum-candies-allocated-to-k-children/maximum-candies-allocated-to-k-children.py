class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 0, max(candies)

        def isSatisfied(num_candies):
            cnt = 0
            for pile in candies:
                cnt += pile // num_candies
            return cnt >= k

        while l < r:
            mid = l + (r - l) // 2 + 1
            if isSatisfied(mid):
                l = mid
            else:
                r = mid - 1
        return r
                