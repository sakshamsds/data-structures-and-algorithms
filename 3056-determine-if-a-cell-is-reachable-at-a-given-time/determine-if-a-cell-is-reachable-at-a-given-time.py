class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        # edge case
        if t == 1 and sx == fx and sy == fy:
            return False

        min_time = max(abs(sx - fx), abs(sy - fy))
        return min_time <= t