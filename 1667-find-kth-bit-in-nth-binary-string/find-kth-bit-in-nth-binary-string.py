class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"

        length = 2 ** n - 1
        mid = length // 2 + 1

        if k < mid:
            return self.findKthBit(n - 1, k)
        elif k == mid:
            return "1"
        else:
            return str(1 ^ int(self.findKthBit(n - 1, 1 + length - k)))
        