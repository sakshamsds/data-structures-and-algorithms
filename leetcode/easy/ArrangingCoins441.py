# import math


class Solution:
    def arrangeCoins(self, n: int) -> int:
        # log(n), binary search, gauss formula
        # left = 1, right = n
        # eg, n = 5,     
        # 1, 2, 3, 4, 5

        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            pdt = mid * (mid + 1) / 2
            if pdt == n:
                return mid
            elif pdt > n:
                right = mid - 1
            else:
                left = mid + 1
        
        return left - 1

        # # quadratic formula
        # return 0.5 * (math.sqrt(1 + 8 * n) - 1)

        # brute force, O(n)
        # i = 0
        # while n>0:
        #     i += 1
        #     n -= i

        # if n < 0:   # we didn't complete last row
        #     i -= 1
        # return i
    
# print(float("inf"))
# print(math.log(5, 2))
# print(Solution().arrangeCoins(2))
# print(Solution().arrangeCoins(4))
# print(Solution().arrangeCoins(5))
# print(Solution().arrangeCoins(8))