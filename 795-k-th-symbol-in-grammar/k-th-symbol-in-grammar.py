'''
1 -                     0
2 -         0                       1
3 -     0       1               1       0
4 -   0   1    1  0          1   0   0    1
'''

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # print(f'row: {n}, idx: {k}')
        if k == 1:
            return 0

        parent = self.kthGrammar(n - 1, (k + 1)//2)
        # print(f'parent: {parent}')

        if parent == 0: # 01
            return 1 if k % 2 == 0 else 0
        else:         # 10    
            return 0 if k % 2 == 0 else 1