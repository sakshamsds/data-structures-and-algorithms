class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles) // 3
        i = len(piles) - 2
        res = 0
        while n > 0:
            res += piles[i]
            i -= 2
            n -= 1
        return res