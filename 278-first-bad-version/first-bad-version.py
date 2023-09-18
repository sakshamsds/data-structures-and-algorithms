# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
# after exiting the while loop, left is the minimal k​ satisfying the condition function;
        l, r = 1, n
        while l < r:
            mid = l + (r - l)//2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1

        return l