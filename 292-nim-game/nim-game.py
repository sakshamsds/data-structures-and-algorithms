'''
1,2,3 win
4, loss
5,6,7 win
8, loss
9,10,11 win
12, loss
'''

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0