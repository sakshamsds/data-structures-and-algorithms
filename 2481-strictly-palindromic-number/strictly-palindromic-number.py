class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2, n - 1):
            num = self.getNumInBaseN(n, base)
            if not self.isPalindrome(num):
                return False
        return True
    
    def getNumInBaseN(self, n: int, base: int) -> str:
        num = ''
        while n > 0:
            num += str(n % base)
            n //= base
        return num

    def isPalindrome(self, num: str):
        for i in range(len(num)//2):
            if num[i] != num[len(num) - 1 - i]:
                return False
        return True