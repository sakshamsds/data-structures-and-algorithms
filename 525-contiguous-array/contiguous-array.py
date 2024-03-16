'''
zeros = 8
ones = 7
1   0   0   1   0   1   1   1   0   0   0   0   0   1   1

0   1   2   2   3   3   3   3   4   5   6   7   8   8   8
1   1   1   2   2   3   4   5   5   5   5   5   5   6   7

0, 0
-1, 0
0, 1
1, 2

0   1

1   1
0   1
'''

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diffMap = {0: -1}
        res = 0

        ones, zeros = 0, 0
        for i, num in enumerate(nums):
            if num == 0:
                zeros += 1
            else:
                ones += 1
            curDiff = zeros - ones
            if curDiff in diffMap:
                res = max(res, i - diffMap[curDiff])
            else:
                diffMap[curDiff] = i
        
        return res
            