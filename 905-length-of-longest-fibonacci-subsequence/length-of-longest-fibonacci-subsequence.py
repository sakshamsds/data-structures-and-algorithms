'''
        1   2   3   4   5   6   7   8
    1       4   3   2   2   2   2   1    
    2           3   2   2   2   1   1
    3               2   2   1   1   1
    4                   1   1   1   1       
    5                       1   1   1
    6                           1   1
    7                               1
    8
'''

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = dict()
        nums_set = set(arr)

        for row in range(n - 2, -1, -1):
            for col in range(n - 1, row, -1):
                x1, x2 = arr[row], arr[col]
                x3 = x1 + x2
                if x3 > arr[-1] or x3 not in nums_set:
                    dp[(x1, x2)] = 1
                else:
                    dp[(x1, x2)] = 1 + dp[(x2, x3)]

        longest_seq = max(dp.values()) + 1
        return longest_seq if longest_seq > 2 else 0