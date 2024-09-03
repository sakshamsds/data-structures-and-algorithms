class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
            
        l, r = 1, num
        while l < r:
            mid = l + (r - l) // 2
            pdt = mid * mid
            if pdt == num:
                return True
            elif pdt > num:
                r = mid
            else:
                l = mid + 1
        return False 