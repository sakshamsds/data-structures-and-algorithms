'''
1 -                     0
2 -         0                       1
3 -     0       1               1       0
4 -   0   1    1  0          1   0   0    1
'''

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        def helper(n, i):
            # print(f'row: {n}, idx: {i}')
            if i == 0:
                return 0

            parent = helper(n - 1, i//2)
            # print(f'parent: {parent}')

            if parent == 0: # 01
                return 0 if i % 2 == 0 else 1
            else:         # 10    
                return 1 if i % 2 == 0 else 0
        
        return helper(n, k - 1)