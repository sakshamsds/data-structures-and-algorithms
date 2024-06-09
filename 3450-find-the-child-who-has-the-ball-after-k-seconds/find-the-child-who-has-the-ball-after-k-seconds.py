class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        turns = k // (n - 1)
        rem = k % (n - 1)
        if turns % 2 == 0:   
            return rem
        return n - 1 - rem