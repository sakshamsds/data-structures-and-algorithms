import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n >= 1 and math.log(n, 2) == int(math.log(n, 2))

        # if n < 1:
            # return False
        
        # while n > 1:
        #     if n % 2 == 0:
        #         n = n // 2
        #     else:
        #         return False
            
        # return True


print(Solution().isPowerOfTwo(1))
print(Solution().isPowerOfTwo(16))
print(Solution().isPowerOfTwo(3))
print(Solution().isPowerOfTwo(-16))