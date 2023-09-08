class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # n & (n - 1), remove number of 1 bits
        
        cnt = 0
        while n > 0:
            n = n & (n - 1)
            cnt += 1
        return cnt
        