class Solution:
    def findComplement(self, num: int) -> int:
        res, k = 0, 0
        while num > 0:
            n = (num % 2) ^ 1
            res += n * 2 ** k 
            k += 1
            num = num >> 1
        return res